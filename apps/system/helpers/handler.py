from abc import ABC, abstractmethod


class AbstractHandler(ABC):

    def __init__(self, request):
        self._req = request

    @abstractmethod
    def exec(self):
        pass
