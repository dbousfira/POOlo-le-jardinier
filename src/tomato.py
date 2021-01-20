from vegetable import Vegetable


class Tomato(Vegetable):
    def grow(self, number=0):
        self.number += number
