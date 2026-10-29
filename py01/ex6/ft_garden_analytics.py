#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        if height >= 0:
            self._height = height
        else:
            self._height = 15.0
        if days >= 0:
            self._days = days
        else:
            self._days = 10
        self._stats = self.Stats()

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
        self._stats._grown += 1
        self.set_height(self.get_height() + height)

    def age(self, days: int) -> None:
        self._stats._aged += 1
        self.set_age(self.get_age() + days)

    @staticmethod
    def more_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return Plant("unknown plant", 0, 0)

    def show(self) -> None:
        self._stats._showed += 1
        name = self._name.capitalize()
        print(f"{name}: {self.get_height():.1f}cm, {self.get_age()} days old")

    class Stats:

        def __init__(self) -> None:
            self._grown = 0
            self._aged = 0
            self._showed = 0

        def display(self) -> None:
            print(f"Stats: {self._grown} grow, {self._aged} age", end="")
            print(f", {self._showed} show")


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


class Seed(Flower):

    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


class Tree(Plant):
    _stats: "Tree.TreeStats"

    def __init__(self, name: str, height: float, days: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = trunk_diameter
        self._stats = self.TreeStats()

    def produce_shade(self) -> None:
        self._stats._shades_produced += 1
        name = self._name.capitalize()
        print(f"Tree {name} now produces a shade of ", end="")
        print(f"{self._height:.1f}cm long", end="")
        print(f" and {self._trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    class TreeStats(Plant.Stats):

        def __init__(self) -> None:
            super().__init__()
            self._shades_produced = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shades_produced} shade")


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


def display_stats(plant: Plant) -> None:
    name = plant._name.capitalize()
    print(f"[statistics for {name}]")
    plant._stats.display()


def main() -> None:
    rose = Flower("rose", 15.0, 10, "red")
    oak = Tree("oak", 200.0, 365, 5.0)
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    anon = Plant.anonymous_plant()

    print("=== Garden Statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.more_than_a_year(30))
    print("Is 400 days more than a year? ->", Plant.more_than_a_year(400))
    print("")
    print("=== Flower")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_stats(rose)
    print("")
    print("=== Tree")
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print("")
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print("")
    print("=== Anonymous")
    anon.show()
    display_stats(anon)


if __name__ == "__main__":
    main()
