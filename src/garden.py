from collections import Counter

from carrot import Carrot
from tomato import Tomato


class Garden():
    """A garden w/ a list of vegetables."""

    def __init__(self) -> None:
        self.vegetables = []
        self.nb = 0

    def _plant(self, cls=Tomato()):
        self.vegetables.append(cls)

    def add(self, vegetable):
        self._plant(vegetable)

        types = [type(v) for v in self.vegetables]
        self.nb = len(Counter(types).keys())

    def seed(self):
        nb = sum([v.number for v in self.vegetables])

        return nb

    def __str__(self) -> str:
        return f"{self.seed()} seeds / {self.nb} types"


if __name__ == "__main__":
    g = Garden()

    c = Carrot()
    g.add(c)
    c.grow(2)

    p = Tomato()
    g.add(p)
    p.grow(8)

    g.seed()
