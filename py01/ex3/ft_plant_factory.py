#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self, height: float) -> None:
        self.height += height

    def age(self, days: int) -> None:
        self.days += days

    def show(self) -> None:
        name = self.name.capitalize()
        print(f"{name}: {self.height:.1f}cm, {self.days} days old")


def main() -> None:
    print("=== Garden Factory Output ===")
    plants = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120),
    ]
    for plant in plants:
        print("Created:", end=" ")
        plant.show()


if __name__ == "__main__":
    main()
