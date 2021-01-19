from carrot import Carrot
from garden import Garden
from tomato import Tomato
from vegetable_factory import VegetableFactory


class Gardener:
    def __init__(self) -> None:
        self.gardens = []
        self.gardens.append(Garden())

    def create_plant(self, cls, nb=1):
        if (self.gardens[-1].seed() + nb > 30):
            print("Garden full!")
            self.gardens.append(Garden())

        vegetable = VegetableFactory.getVegetable(cls)

        if vegetable is not None:
            vegetable.grow(nb)
            self.gardens[-1].add(vegetable)
        else:
            print(f"Unknown vegetable {cls}!")


if __name__ == "__main__":
    g = Gardener()

    g.create_plant("carrot")
    g.create_plant("tomato")
    g.create_plant("tomato", 28)
    g.create_plant("banana")

    print(*g.gardens)
