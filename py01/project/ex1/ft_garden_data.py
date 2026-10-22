#!/usr/bin/env python3

class Plant:
    _name: str
    _height: int
    _age: int

    def show(self):
        print(f"{self._name.capitalize()}: {self._height}cm, {self._age} days old")

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant()
    rose._name = "Rose"
    rose._height = 25
    rose._age = 30

    sunflower = Plant()
    sunflower._name = "Sunflower"
    sunflower._height = 80
    sunflower._age = 45

    cactus = Plant()
    cactus._name = "Cactus"
    cactus._height = 15
    cactus._age = 120
    
    rose.show()
    sunflower.show()
    cactus.show()
