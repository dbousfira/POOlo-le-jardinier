from vegetable import Vegetable


class Onion(Vegetable):
    def grow(self, number=0):
        self.number += number