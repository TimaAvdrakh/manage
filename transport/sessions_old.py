from __future__ import print_function
import sys
import socket
import select
import time
import threading
import typing
from dataclasses import dataclass

import pyasn1.error as asn1_error
from pyasn1.codec.ber.decoder import decode as ber_decode

from apps.system.lib import (
    exceptions,
    logger,
    asn1,
)
from apps.kernel.infrastructure.messaging import base
from apps.kernel.infrastructure.messaging.session import (
    connect,
    adjustment,
)
from apps.kernel.infrastructure.messaging.trap import trap
from apps.kernel.infrastructure.messaging.report import report
from apps.kernel.infrastructure.messaging.unformatted import unformatted


@dataclass
class ChannelParameters:
    inactivity_timeout: int
    max_data_length: int
    data_packet_window_size: int
    data_load_timeout: int
    request_response_timeout: int
    data_packet_response_timeout: int


class Channel:

    def __init__(self, id_, host, port):
        self.lg = logger.instance()
        self.id = id_
        self.host = host
        self.port = port
        self.sock = None
        self.channel_parameters = ChannelParameters(60, 1000, 5, 60, 60, 60)
        self.undecoded_data = bytes()
        self.expired_inactivity_timeouts = 0
        self.last_activity_time = time.time()
        self.message_dispatching_thread = threading.Thread(
            name=(self.__class__.__name__ + '-MessageDispatcher'),
            target=(self.message_dispatcher)
        )
        self.stop_message_dispatching_event = threading.Event()
        self.last_heartbeat_trap = None
        self.heartbeat_thread = threading.Thread(
            name=(self.__class__.__name__ + '-Heartbeat'),
            target=(self.heartbeat)
        )
        self.stop_heartbeat_event = threading.Event()
        self.not_responded_requests = {}
        self.message_handlers = {}
        self.user_message_handlers = {}
        self.initialized = False
        self.there_were_errors = False
        self.message_handlers.update({
            connect.ConnectResponse.__name__: self.handle_connect_response,
            adjustment.AdjustmentResponse.__name__: self.handle_adjustment_response,
            trap.HeartbeatTrap.__name__: self.handle_trap,
            trap.RestartSoftwareTrap.__name__: self.handle_trap,
            trap.UnauthorizedAccessTrap.__name__: self.handle_trap,
            trap.CriticalErrorTrap.__name__: self.handle_trap,
            trap.MajorErrorTrap.__name__: self.handle_trap,
            trap.MinorErrorTrap.__name__: self.handle_trap,
            trap.TrapAck.__name__: self.handle_trap_ack,
        })

    def get_full_name(self):
        return f'#{self.id} ({self.host}:{self.port})'

    def open(self):
        self.lg.diagnostic(
            f'Opening connection for the channel {self.get_full_name()}...'
        )
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.setblocking(False)

    def close(self):
        self.stop_heartbeat()
        self.wait_for_requests_completion(3)
        self.stop_message_dispatcher()
        if self.sock is not None:
            self.lg.diagnostic(
                f'Closing connection for the channel {self.get_full_name()}...'
            )
            self.sock.close()
            self.sock = None
        if len(self.not_responded_requests) > 0:
            self.there_were_errors = True
            self.lg.error('There are not responded requests:')
            for request in self.not_responded_requests.values():
                self.lg.error(f'    {request}')

            self.not_responded_requests.clear()
        self.initialized = False

    def initialize(self, cp_: ChannelParameters):
        self.channel_parameters = cp_
        self.open()
        self.start_message_dispatcher()
        self.send_request(
            connect.ConnectRequest(
                cp_.inactivity_timeout,
                cp_.max_data_length,
                cp_.data_packet_window_size,
                cp_.data_load_timeout,
                cp_.request_response_timeout,
                cp_.data_packet_response_timeout
            )
        )

    def wait_for_initialization(self, timeout):
        finish = time.time() + timeout
        while time.time() < finish:
            if self.initialized:
                return True
            time.sleep(0.01)

        return self.initialized

    def send_message(self, message):
        encoded_data = message.encode()
        rest_size = len(encoded_data)
        self.lg.diagnostic(
            f'Sending the {message.__class__.__name__,} message on t' +
            f'he channel {self.get_full_name()}...'
        )
        self.lg.debug(
            f'The message to send: {message}'
        )
        self.lg.log_memory_dump(
            logger.llvl_debug, 'Data to send:', encoded_data
        )
        while rest_size > 0:
            ready = select.select([], [self.sock.fileno()], [], 0.2)
            if len(ready[1]) > 0:
                rest_size -= self.sock.send(encoded_data[-rest_size:])

    def send_request(self, request):
        self.not_responded_requests.update({request.message_id: request})
        self.send_message(request)

    def register_incoming_message(self, message):
        request = self.not_responded_requests.pop(message.message_id, None)
        if request is not None:
            return request
        raise exceptions.GeneralFault(
            f'unable to find sent request for received response' +
            f' {message.__class__.__name__} (message_id: {message.message_id})'
        )

    def wait_for_requests_completion(self, timeout):
        finish = time.time() + timeout
        while time.time() < finish:
            if len(self.not_responded_requests) == 0:
                return True
            time.sleep(0.01)

        return len(self.not_responded_requests) == 0

    def receive_data(self, callback):
        ready = select.select([self.sock], [], [], 0.2)
        if len(ready[0]) > 0:
            callback(self.sock.recv(4096))

    def inactivity_timeout_expired(self):
        self.expired_inactivity_timeouts += 1
        if self.expired_inactivity_timeouts >= 3:
            self.close()
            return
        self.last_heartbeat_trap = trap.HeartbeatTrap(None, None)
        self.send_request(self.last_heartbeat_trap)

    def register_activity(self):
        self.expired_inactivity_timeouts = 0
        self.last_activity_time = time.time()

    def have_errors(self):
        return self.there_were_errors

    def start_message_dispatcher(self):
        self.lg.diagnostic(
            f'Starting message dispatcher on the channel {self.get_full_name()}...'
        )
        self.message_dispatching_thread.start()

    def stop_message_dispatcher(self):
        if self.message_dispatching_thread.is_alive():
            if not self.stop_message_dispatching_event.is_set():
                self.lg.diagnostic(
                    f'Stopping message dispatcher on the channel {self.get_full_name()}...'
                )
                self.stop_message_dispatching_event.set()
                if threading.current_thread().ident != self.message_dispatching_thread.ident:
                    self.message_dispatching_thread.join()

    def message_dispatcher(self):
        try:
            while not self.stop_message_dispatching_event.is_set():
                message = self.wait_for_message()
                if message is None:
                    pass
                else:
                    handler = self.message_handlers.get(
                        message.__class__.__name__, self.default_handler
                    )
                    handler(message)

        except Exception as e:
            self.there_were_errors = True
            self.lg.critical(
                f'Unexpected error occurred while messages dispatching' +
                f' on the channel {self.get_full_name()}: {str(e)}'
            )
            self.lg.log_back_trace(logger.llvl_critical, sys.exc_info()[2])

    def set_user_message_handler(self, class_reference, function):
        self.user_message_handlers[class_reference.__name__] = function

    def reset_user_message_handler(self, class_reference_):
        del self.user_message_handlers[class_reference_.__name__]

    def wait_for_message(self):

        def append_data(data_):
            self.undecoded_data = self.undecoded_data + data_

        raw_message = None
        while True:
            if self.stop_message_dispatching_event.is_set():
                return
            self.receive_data(append_data)
            try:
                raw_message, rest = ber_decode(
                    self.undecoded_data, asn1.SkrMessage()
                )
                self.undecoded_data = rest
                break
            except asn1_error.SubstrateUnderrunError:
                continue

        message = base.create_typed_message(raw_message)
        self.lg.diagnostic(
            f'The {message.__class__.__name__} message has been received ' +
            f'on the channel {self.get_full_name()} ...'
        )
        self.lg.debug(f'The message body: {message}')
        return message

    def default_handler(self, message_):
        request = None if isinstance(
            message_, report.BaseReport
        ) or isinstance(
            message_, unformatted.RawReport
        ) else self.register_incoming_message(message_)
        if not self.run_user_handler(request, message_):
            self.lg.warning(
                f'No handler is defined for ' +
                f'the "{message_.__class__.__name__}" received message'
            )

    def run_user_handler(self, request_, incoming_message):
        handler = self.user_message_handlers.get(
            incoming_message.__class__.__name__, None
        )
        if handler is not None and callable(handler):
            handler(self, request_, incoming_message)
            return True
        else:
            return False

    def start_heartbeat(self):
        self.lg.diagnostic(
            f'Starting heartbeat on the channel {self.get_full_name()}...'
        )
        self.heartbeat_thread.start()

    def stop_heartbeat(self):
        if self.heartbeat_thread.is_alive():
            if not self.stop_heartbeat_event.is_set():
                self.lg.diagnostic(
                    'Stopping heartbeat on the channel {self.get_full_name()}.'
                )
                self.stop_heartbeat_event.set()
                if threading.current_thread().ident != self.heartbeat_thread.ident:
                    self.heartbeat_thread.join()

    def heartbeat(self):
        seconds_to_expiry = time.time() - self.last_activity_time + self.channel_parameters.inactivity_timeout
        while not self.stop_heartbeat_event.is_set():
            seconds_to_expiry -= 1
            if seconds_to_expiry > 0:
                time.sleep(1)
            else:
                self.inactivity_timeout_expired()
                self.last_activity_time = time.time()
                seconds_to_expiry = time.time() - self.last_activity_time + self.channel_parameters.inactivity_timeout

    def handle_connect_response(self, response):
        request = self.register_incoming_message(response)
        self.run_user_handler(request, response)
        self.send_request(adjustment.AdjustmentRequest(response.supports))

    def handle_adjustment_response(self, response):
        request = self.register_incoming_message(response)
        self.run_user_handler(request, response)
        self.initialized = True

    def handle_trap(self, message):
        self.send_message(trap.TrapAck(message.message_id))
        self.run_user_handler(None, message)

    def handle_trap_ack(self, message):
        request = self.register_incoming_message(message)
        if message.message_id == self.last_heartbeat_trap.message_id:
            self.last_heartbeat_trap = None
        else:
            self.lg.warning(
                f'Ignoring trap ack for the old {trap.Trap.__name__} heartbeat trap...'
            )
        self.run_user_handler(request, message)


ChannelsList = typing.List[Channel]


class Session:

    @staticmethod
    def create_channels_list() -> ChannelsList:
        return [None, None, None, None, None]

    def __init__(self, host, channel_ports):
        if len(channel_ports) != 5:
            raise exceptions.GeneralFault(
                f'5 channel ports required, but {len(channel_ports)} are provided'
            )
        self.lg = logger.instance()
        self.channels = self.create_channels_list()
        self.there_were_errors = False
        channel_id = 0
        have_channels = False
        for port in channel_ports:
            channel_id += 1
            if port is not None:
                have_channels = True
                self.channels[channel_id - 1] = Channel(channel_id, host, port)

        if not have_channels:
            raise exceptions.GeneralFault('no one channel port is provided')

    def initialize(self, cp_: ChannelParameters):
        for channel in self.channels:
            if channel is not None:
                channel.initialize(cp_)
                if not channel.wait_for_initialization(10):
                    raise Exception(
                        f'unable to initialize the ' +
                        f'channel {channel.get_full_name()}'
                    )

    def channel(self, channel_id):
        return self.channels[(channel_id - 1)]

    def register_error(self, message):
        self.there_were_errors = True
        self.lg.error(message)

    def have_errors(self):
        if self.there_were_errors:
            return True
        else:
            for channel in self.channels:
                if channel is not None:
                    self.there_were_errors = self.there_were_errors or channel.have_errors()

            return self.there_were_errors

    def finalize(self):
        for channel in self.channels:
            if channel is not None:
                channel.close()
