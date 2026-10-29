#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        name = self.name.capitalize()
        print(f"{name}: {self.height}cm, {self.days} days old")


def main() -> None:
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
