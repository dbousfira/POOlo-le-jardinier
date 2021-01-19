from carrot import Carrot
from tomato import Tomato


class VegetableFactory:

    def getVegetable(vegetable):
        """Get object of type vegetable.

        Args:
            vegetable (Vegetable): name of the vegetable

        Returns:
            Vegetable or None: the new vegetable on None if not exist
        """
        if vegetable is None:
            return None

        vegetable = vegetable.upper()

        if vegetable == "carrot".upper():
            return Carrot()
        elif vegetable == "tomato".upper():
            return Tomato()
