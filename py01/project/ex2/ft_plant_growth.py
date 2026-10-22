#!/usr/bin/env python3

class Plant:
    _name: str
    _height: float
    _age: int

    def grow(self, _height=0.8):
        self._height += _height

    def age(self, days=1):
        self._age += days

    def show(self):
        print(f"{self._name.capitalize()}: {self._height:.1f}cm, {self._age} days old")

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    initial_height = 25

    rose = Plant()
    rose._name = "Rose"
    rose._height = initial_height
    rose._age = 30
    rose.show()

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()

    diff = rose._height - initial_height
    print(f"Growth this week: {diff:.1f}cm")
