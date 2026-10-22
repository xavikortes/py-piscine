#!/usr/bin/env python3

class Plant():
    _name: str
    _height: float
    _age: int

    def __init__(self, _name: str, _height: float, _age: int):
        self._name = _name
        if _height >= 0:
            self._height = _height
        else:
            self._height = 15.0
        if _age >= 0:
            self._age = _age
        else:
            self._age = 10
        self._stats = self.Stats()

    def grow(self, _height=0.8):
        self.set_height(self._height + _height)
        self._stats._grown += 1

    def age(self, days=1):
        self.set_age(self._age + days)
        self._stats._aged += 1

    def get_height(self) -> float:
        return self._height

    def set_height(self, _height: float) -> None:
        if _height < 0:
            print(f"{self._name}: Error, height can't be negative\nHeight update rejected")
        else:
            self._height = _height

    def get_age(self) -> int:
        return self._age

    def set_age(self, _age: int):
        if _age < 0:
            print(f"{self._name}: Error, age can't be negative\nAge update rejected")
        else:
            self._age = _age

    @staticmethod
    def more_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous_plant(cls):
        return Plant("Unknown plant", 0, 0)

    def show(self):
        print(f"{self._name.capitalize()}: {self.get_height():.1f}cm, {self.get_age()} days old")
        self._stats._showed += 1

    class Stats():
        _grown: int
        _aged: int
        _showed: int

        def __init__(self):
            self._grown = 0
            self._aged = 0
            self._showed = 0

        def display(self):
            print(f"Stats: {self._grown} grow, {self._aged} age, {self._showed} show")

class Flower(Plant):
    _color: str
    _blommed: bool

    def __init__(self, _name: str, _height: float, _age: int, _color: str):
        super().__init__(_name, _height, _age)
        self._color = _color
        self._blommed = False

    def bloom(self):
        self._blommed = True

    def show(self):
        super().show()
        print(f" Color: {self._color}")
        if self._blommed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")
    
class Seed(Flower):
    _seeds: int

    def __init__(self, _name: str, _height: float, _age: int, _color: str):
        super().__init__(_name, _height, _age, _color)
        self._seeds = 0

    def bloom(self):
        self._seeds = 42

    def show(self):
        super().show()
        print(f" Seeds: {self._seeds}")

class Tree(Plant):
    _trunk_diameter: float

    def __init__(self, _name: str, _height: float, _age: int, _trunk_diameter: float):
        super().__init__(_name, _height, _age)
        self._trunk_diameter = _trunk_diameter
        self._stats = self.Stats()

    def produce_shade(self):
        self._stats._shades_produced += 1
        print(f"Tree {self._name} now produces a shade of {self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide.")

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    class Stats(Plant.Stats):
        _shades_produced: int

        def __init__(self):
            super().__init__()
            self._shades_produced = 0

        def display(self):
            super().display()
            print(f" {self._shades_produced} shade")

class Vegetable(Plant):
    _harvest_season: str
    _nutritional_value: int
    _has_grown: bool
    _has_aged: bool

    def __init__(self, _name: str, _height: float, _age: int, _harvest_season: str, _nutritional_value: int):
        super().__init__(_name, _height, _age)
        self._harvest_season = _harvest_season
        self._nutritional_value = _nutritional_value
        self._has_grown = False
        self._has_aged = False

    def grow(self, _height=0.8):
        super().grow(_height)
        if self._has_aged:
            self._nutritional_value += 1
            self._has_aged = False
        else:
            self._has_grown = True

    def age(self):
        super().age()
        if self._has_grown:
            self._nutritional_value += 1
            self._has_grown = False
        else:
            self._has_aged = True

    def show(self):
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

def display_stats(plant: Plant):
    print(f"[statistics for {plant._name}]")
    plant._stats.display()

if __name__ == "__main__":
    print("=== Garden Statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.more_than_a_year(30))
    print("Is 400 days more than a year? ->", Plant.more_than_a_year(400))
    print("")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_stats(rose)
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print("")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print("")
    print("=== Anonymous")
    anon = Plant.anonymous_plant()
    anon.show()
    display_stats(anon)
