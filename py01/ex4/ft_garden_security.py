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

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            name = self._name.capitalize()
            print(f"{name}: Error, height can't be negative")
            print("Height update rejected")
            return

        self._height = height
        print(f"Height updated: {height:.0f}cm")

    def get_age(self) -> int:
        return self._days

    def set_age(self, days: int) -> None:
        if days < 0:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
            return

        self._days = days
        print(f"Age updated: {days} days")

    def grow(self, height: float) -> None:
        self.set_height(self.get_height() + height)

    def age(self, days: int) -> None:
        self.set_age(self.get_age() + days)

    def show(self) -> None:
        name = self._name.capitalize()
        print(f"{name}: {self.get_height():.1f}cm, {self.get_age()} days old")


def main() -> None:
    rose = Plant("Rose", -1, -1)
    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    rose.show()
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-25)
    rose.set_age(-25)
    print("")
    print("Current state:", end=" ")
    rose.show()


if __name__ == "__main__":
    main()
