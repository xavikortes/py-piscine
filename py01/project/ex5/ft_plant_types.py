#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        if height > 0:
            self._height = height
        else:
            self._height = 15.0
        if days > 0:
            self._days = days
        else:
            self._days = 10

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            name = self._name.capitalize()
            print(f"{name}: Error, height can't be negative")
            print("Height update rejected")
            return

        self._height = height

    def get_age(self) -> int:
        return self._days

    def set_age(self, days: int) -> None:
        if days < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
            return

        self._days = days

    def grow(self, height: float) -> None:
        self.set_height(self.get_height() + height)

    def age(self, days: int) -> None:
        self.set_age(self.get_age() + days)

    def show(self) -> None:
        name = self._name.capitalize()
        print(f"{name}: {self.get_height():.1f}cm, {self.get_age()} days old")


class Flower(Plant):

    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days)
        self._color = color
        self._blommed = False

    def bloom(self) -> None:
        self._blommed = True

    def show(self) -> None:
        super().show()
        name = self._name.capitalize()
        print(f" Color: {self._color}")
        if self._blommed:
            print(f" {name} is blooming beautifully!")
        else:
            print(f" {name} has not bloomed yet")


class Tree(Plant):

    def __init__(self, name: str, height: float, days: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        name = self._name.capitalize()
        print(f"Tree {name} now produces a shade of ", end="")
        print(f"{self._height:.1f}cm long", end="")
        print(f" and {self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):

    def __init__(self, name: str, height: float, days: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, days)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value
        self._has_grown = False
        self._has_aged = False

    def grow(self, height: float) -> None:
        super().grow(height)
        self._has_grown = True
        self.add_nutritional_value()

    def age(self, days: int) -> None:
        super().age(days)
        self._has_aged = True
        self.add_nutritional_value()

    def add_nutritional_value(self) -> None:
        if not self._has_grown or not self._has_aged:
            return
        self._nutritional_value += 1
        self._has_grown = False
        self._has_aged = False

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


def main() -> None:
    rose = Flower("rose", 15.0, 10, "red")
    oak = Tree("oak", 200.0, 365, 5.0)
    tomato = Vegetable("tomato", 5.0, 10, "April", 0)

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("")
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("")
    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow(2.1)
        tomato.age(1)
    tomato.show()


if __name__ == "__main__":
    main()
