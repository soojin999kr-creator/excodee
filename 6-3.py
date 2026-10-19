from abc import ABC, abstractmethod

class AbstractPolygon(ABC):
    def __init__(self, numSide):
        self.sideNumber = numSide
        self.sideLen = 0.0

    def setSideLen(self, sideLen):
        self.sideLen = float(sideLen)

    @abstractmethod
    def getArea(self):
        pass

class TestRect(AbstractPolygon):
    def __init__(self):
        super().__init__(4)

    def getArea(self):
        return self.sideLen * self.sideLen
