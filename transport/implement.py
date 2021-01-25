import time
from queue import Queue

from redis import Redis

from transport import abstract


class RedisReceiverBroker(abstract.AbstractReceiver):

    def __init__(self, name, redis_inst=None):
        super().__init__(name)
        self.rds = redis_inst

        if self.rds is None:
            raise Exception('Не указано подключение к Redis')

    def listener(self, queue: Queue, *args, **kwargs) -> None:
        while True:
            data = self.rds.lpop(self._name)
            if data and len(data) > 0:
                queue.put(data)
            time.sleep(1)


class RedisSenderBroker(abstract.AbstractSender):

    def __init__(self, name, redis_inst=None):
        super().__init__(name)
        self.rds = redis_inst

        if self.rds is None:
            raise Exception('Не указано подключение к Redis')

    def send_message(self, message, *args, **kwargs):
        self.rds.lpush(self._name, message)
