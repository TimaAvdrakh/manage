import time


class Worker:

    def __init__(self, host: str, ports: []):
        self._host = host
        self._ports = ports

    def run(self):
        print(self._host, self._ports)

        i = 0
        while True:
            print(f'{self._host}) Hi mir: {i}')
            if i > 10:
                break

            i += 1
            time.sleep(1)
        print(f'{self._host}) Goodbye: {i}')
