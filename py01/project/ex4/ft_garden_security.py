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
        print("Plant created:", end=" ")
        self.show()

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
            print(f"Height updated: {self._height:.0f}cm")

    def get_age(self) -> int:
        return self._age

    def set_age(self, _age: int):
        if _age < 0:
            print(f"{self._name}: Error, age can't be negative\nAge update rejected")
        else:
            self._age = _age
            print(f"Age updated: {self._age} days")

    def show(self):
        print(f"{self._name.capitalize()}: {self.get_height():.1f}cm, {self.get_age()} days old")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 0, 0)
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-25)
    rose.set_age(-25)
    print("")
    print("Current state:", end=" ")
    rose.show()
