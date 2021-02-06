from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def getArea(self):
        pass
