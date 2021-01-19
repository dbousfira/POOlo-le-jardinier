from vegetable import Vegetable


class Carrot(Vegetable):
    """[summary]

    Args:
        Vegetable ([type]): [description]
    """
    def grow(self, number=0):
        self.number += number