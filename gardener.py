from garden import Garden
from vegetable_factory import VegetableFactory


class Gardener:
    """"A gardener w/ a list of gardens."""

    def __init__(self) -> None:
        self.gardens = []
        self.gardens.append(Garden())

    def create_plant(self, cls, nb=1):
        """Create plants using VegetableFactory.

        Args:
            cls (str): vegetable name,
            nb (int, optional): number of seeds. Defaults to 1.
        """
        if (nb > 30):
            print("Number of seeds max is 30!")
            return

        if (self.gardens[-1].seed() + nb > 30):
            print("Garden full!")
            self.gardens.append(Garden())

        vegetable = VegetableFactory.getVegetable(cls)

        if vegetable:
            vegetable.grow(nb)
            self.gardens[-1].add(vegetable)
        else:
            print(f"Unknown vegetable {cls}!")
            self.gardens.pop()


if __name__ == "__main__":
    poolo = Gardener()

    poolo.create_plant("carrot")
    poolo.create_plant("tomato")
    poolo.create_plant("tomato", 28)
    poolo.create_plant("banana")
    poolo.create_plant("carrot", 60)

    print(*poolo.gardens, sep="\n")
