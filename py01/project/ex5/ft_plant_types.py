#!/usr/bin/env python3

class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, _name: str, _height: float, _age: int):
        self._name = _name
        if _height > 0:
            self._height = _height
        else:
            self._height = 15.0
        if _age > 0:
            self._age = _age
        else:
            self._age = 10

    def grow(self, _height=0.8):
        self.set_height(self._height + _height)

    def age(self, days=1):
        self.set_age(self._age + days)

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

    def show(self):
        print(f"{self._name.capitalize()}: {self.get_height():.1f}cm, {self.get_age()} days old")

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

class Tree(Plant):
    _trunk_diameter: float

    def __init__(self, _name: str, _height: float, _age: int, _trunk_diameter: float):
        super().__init__(_name, _height, _age)
        self._trunk_diameter = _trunk_diameter

    def produce_shade(self):
        print(f"Tree {self._name} now produces a shade of {self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide.")

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

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

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("")
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow(2.1)
        tomato.age()
    tomato.show()
