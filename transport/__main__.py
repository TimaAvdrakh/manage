import time
from threading import Thread
from queue import Queue

import redis

from transport import (
    abstract,
    implement,
    session,
)

r = redis.Redis(host='localhost', port=6379, db=0)


def internal_receiver(name: str, queue_out: Queue) -> None:
    while True:
        data = r.lpop(name)
        print(f'RECEV: {data}')
        if data is not None:
            queue_out.put(data)
        time.sleep(1)


def main():

    response_channel_1 = implement.RedisSenderBroker(
        name='resp_channel_1', redis_inst=r
    )
    request_channel_1 = implement.RedisReceiverBroker(
        name='req_channel_1', redis_inst=r
    )

    q_in = Queue()
    q_out = Queue()

    chan1 = session.Channel(q_in, q_out)
    chan1.start()

    q_in.put(session.ClientCommand(type_=0, data=('127.0.0.1', 8881)))

    q_in.put(session.ClientCommand(type_=1, data='SUPER GUUD'))
    q_in.put(session.ClientCommand(type_=2))

    time.sleep(3)
    q_in.put(session.ClientCommand(type_=2))

    if not q_out.empty():
        print('RES SND: ', str(q_out.get(timeout=3)))

    q_in.put(session.ClientCommand(type_=3))

    time.sleep(5)

    chan1.join()


if __name__ == '__main__':
    main()
