from abc import ABC, abstractmethod


class Vegetable(ABC):
    def __init__(self) -> None:
        self.number = 0

    @abstractmethod
    def grow(self, number=0):
        pass