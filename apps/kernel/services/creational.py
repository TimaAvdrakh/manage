import multiprocessing as mp

from apps.system.helpers import singleton

from apps.kernel import models
from apps.kernel.workers import worker


class WorkerCreator(metaclass=singleton.Singleton):
    workers = {}

    def __init__(self):
        pass

    def up(self):
        com_obj = models.CommunicationObject.objects.filter(state=True).all()

        for obj in com_obj:
            w = worker.Worker(obj.ip_address, obj.port.split('.'))
            p = mp.Process(target=w.run)
            self.workers[obj.id] = p

        for k, v in self.workers.items():
            v.start()

    def kill_proc(self, pid):
        if pid in self.workers.keys():
            self.workers[pid].kill()

    def start_proc(self, pid: int):
        if pid not in self.workers.keys():
            obj = models.CommunicationObject.objects.filter(id=pid).first()
            w = worker.Worker(obj.ip_address, obj.port.split('.'))
            p = mp.Process(target=w.run)
            self.workers[obj.id] = p
            p.start()
