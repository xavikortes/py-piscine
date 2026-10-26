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
    initial_height = 25
    rose = Plant("rose", initial_height, 30)

    print("=== Garden Plant Growth ===")
    rose.show()

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow(0.8)
        rose.age(1)
        rose.show()

    diff = rose.height - initial_height
    print(f"Growth this week: {diff:.1f}cm")


if __name__ == "__main__":
    main()
