from abc import ABC, abstractmethod


class AbstractHandler(ABC):

    @abstractmethod
    def exec(self):
        pass
