from os import O_NOINHERIT
from vegetable import Vegetable


class Carrot(Vegetable):
    def grow(self, number=0):
        self.number += number
