from queue import Queue


class AbstractReceiver(object):

    def __init__(self, name: str):
        """
        :param name: str
            Queue name
        """
        self._name = name

    def listener(self, queue: Queue, *args, **kwargs) -> None:
        """
        :param queue: Queue
            Native python queue
        :return:
        """
        raise NotImplementedError


class AbstractSender(object):

    def __init__(self, name: str):
        """
        :param name: str
            Queue name
        """
        self._name = name

    def send_message(self, message, *args, **kwargs):
        """
        :param message:
            Any type send
        :return:
        """
        raise NotImplementedError
