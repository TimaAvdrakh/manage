import socket
import select
import time
import struct
from queue import Queue
from threading import Thread, Event
from typing import Optional

from transport.abstract import AbstractSender, AbstractReceiver


class Channel1:

    def __init__(self, id_: int, host: str, port: int, sender: AbstractSender,
                 receiver: AbstractReceiver):
        self._id = id_
        self.host = host
        self.port = port
        self.broker = sender
        self.receiver = receiver

        self.sock = None
        # self.data_input_dispatching_thread = None
        # self.data_output_dispatching_thread = None
        self.stop_data_dispatching_event = Event()

    def open(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.setblocking(False)

    def close(self):
        if self.sock is not None:
            self.sock.close()
            self.sock = None

    def send_message(self, message):
        print(f'MSG: {message},\nSOK: {self.sock}')
        if isinstance(message, bytes):
            encoded_data = message
        else:
            encoded_data = message.encode()

        rest_size = len(encoded_data)

        while rest_size > 0:
            ready = select.select([], [self.sock.fileno()], [], 0.2)
            if len(ready[1]) > 0:
                rest_size -= self.sock.send(encoded_data[-rest_size:])

    def _wait_for_data(self) -> bytes:
        undecoded_data = bytes()

        ready = select.select([self.sock], [], [], 0.2)
        if len(ready[0]) > 0:
            undecoded_data += self.sock.recv(4096)

        return undecoded_data

    def _sending_data(self, queue: Queue):
        while True:
            data = queue.get()
            if data and len(data) > 0:
                print(f'DA: {data}')
                self.send_message(data)
            time.sleep(.03)

    def data_input_dispatcher(self):
        print('data_input_dispatcher')
        try:
            while not self.stop_data_dispatching_event.is_set():
                data = self._wait_for_data()
                if len(data) > 0:
                    self.broker.send_message(data)
                else:
                    pass
                time.sleep(1)

        except Exception as e:
            print(
                f'Unexpected error occurred while messages dispatching' +
                f' on the channel {self._id}: {str(e)}'
            )

    def data_output_dispatcher(self):
        print('data_output_dispatcher')
        queue = Queue()

        t1 = Thread(target=self.receiver.listener, args=(queue,))
        t2 = Thread(target=self._sending_data, args=(queue,))

        t2.start()
        t1.start()

        t1.join()
        t2.join()

    def start_data_dispatcher(self):
        data_input_dispatching_thread = Thread(
            name=(self.__class__.__name__ + '-DataDispatcher'),
            target=self.data_input_dispatcher
        )
        data_output_dispatching_thread = Thread(
            name=(self.__class__.__name__ + '-DataDispatcher'),
            target=self.data_output_dispatcher
        )

        # self.data_input_dispatching_thread.start()
        data_output_dispatching_thread.start()


class ClientCommand(object):
    """ A command to the client thread.
        Each command type has its associated data:

        CONNECT:    (host, port) tuple
        SEND:       Data string
        RECEIVE:    None
        CLOSE:      None
    """
    CONNECT, SEND, RECEIVE, CLOSE = range(4)

    def __init__(self, type_, data=None):
        self.type_of_data = type_
        self.data = data

    def __str__(self):
        return f'Type: {self.type_of_data}\nData: {self.data}'


class ClientReply(object):
    """ A reply from the client thread.
        Each reply type has its associated data:

        ERROR:      The error string
        SUCCESS:    Depends on the command - for RECEIVE it's the received
                    data string, for others None.
    """
    ERROR, SUCCESS = range(2)

    def __init__(self, type_, data=None):
        self.type_of_data = type_
        self.data = data

    def __str__(self):
        return f'Type: {self.type_of_data}\nData: {self.data}'


class Channel(Thread):

    def __init__(self, cmd_q: Queue = None, reply_q: Queue = None):
        super().__init__()

        self.cmd_q = cmd_q or Queue()
        self.reply_q = reply_q or Queue()
        self.alive = Event()
        self.alive.set()
        self.socket: socket.socket = None
        self.handlers = {
            ClientCommand.CONNECT: self._handle_CONNECT,
            ClientCommand.CLOSE: self._handle_CLOSE,
            ClientCommand.SEND: self._handle_SEND,
            ClientCommand.RECEIVE: self._handle_RECEIVE,
        }

    def run(self):
        while self.alive.isSet():
            try:
                cmd: ClientCommand = self.cmd_q.get(True, 0.1)
                self.handlers[cmd.type_of_data](cmd)
            except Exception as e:
                continue

    def join(self, timeout: Optional[float] = ...) -> None:
        self.alive.clear()
        if self.is_alive():
            super().join()

    def _handle_CONNECT(self, cmd: ClientCommand):
        try:
            self.socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM
            )
            self.socket.connect((cmd.data[0], cmd.data[1]))
            self.socket.setblocking(False)
            self.reply_q.put(self._success_reply('CONNECT SUCCESS'))
        except IOError as e:
            self.reply_q.put(self._error_reply(e))

    def _handle_CLOSE(self, cmd: ClientCommand):
        self.socket.close()
        reply = ClientReply(ClientReply.SUCCESS)
        self.reply_q.put(reply)

    def _handle_SEND(self, cmd: ClientCommand):
        print(f'SEND handle: {str(cmd)}')
        if isinstance(cmd.data, bytes):
            encoded_data = cmd.data
        else:
            encoded_data = cmd.data.encode()

        try:
            self.socket.sendall(encoded_data)
            self.reply_q.put(self._success_reply())
        except Exception as e:
            print(e)
            self.reply_q.put(self._error_reply(str(e)))

    def _handle_RECEIVE(self, cmd: ClientCommand):
        print('RUN RECV!')
        try:
            data = self._wait_for_data()
            print(f'RECV: {data}')
            if len(data) > 0:
                self.reply_q.put(data)
            else:
                pass
        except IOError as e:
            self.reply_q.put(self._error_reply(str(e)))

    def _error_reply(self, errstr):
        return ClientReply(ClientReply.ERROR, errstr)

    def _success_reply(self, data=None):
        return ClientReply(ClientReply.SUCCESS, data)

    def _wait_for_data(self) -> bytes:
        undecoded_data = bytes()
        ready = select.select([self.socket], [], [], 0.2)
        if len(ready[0]) > 0:
            undecoded_data += self.socket.recv(4096)
        return undecoded_data
