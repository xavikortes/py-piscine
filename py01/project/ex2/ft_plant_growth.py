#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age: int

    def grow(self, height=0.8):
        self.height += height

    def age(self, days=1):
        self.age += days

    def show(self):
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.age} days old")

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    initial_height = 25

    rose = Plant()
    rose.name = "Rose"
    rose.height = initial_height
    rose.age = 30
    rose.show()

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()

    diff = rose._height - initial_height
    print(f"Growth this week: {diff:.1f}cm")
