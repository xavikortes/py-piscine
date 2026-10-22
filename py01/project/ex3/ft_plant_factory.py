#!/usr/bin/env python3

class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, _name: str, _height: float, _age: int):
        self._name = _name
        self._height = _height
        self._age = _age
        print("Created:", end=" ")
        self.show()

    def grow(self, _height=0.8):
        self._height += _height

    def age(self, days=1):
        self._age += days

    def show(self):
        print(f"{self._name.capitalize()}: {self._height:.1f}cm, {self._age} days old")

if __name__ == "__main__":
    print("=== Garden Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
