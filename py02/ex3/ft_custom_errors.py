#!/usr/bin/env python3

class GardenError(Exception):

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or "Unknown garden error")


class PlantError(GardenError):

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or "Unknown plant error")


class WaterError(GardenError):

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or "Unknown water error")


def garden_operations(error: str) -> None:
    match (error):
        case "PlantError":
            raise PlantError("The tomato plant is wilting!")
        case "WaterError":
            raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("Testing PlantError...")
    try:
        garden_operations("PlantError")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("")

    print("Testing WaterError...")
    try:
        garden_operations("WaterError")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("")

    print("Testing catching all garden errors...")
    try:
        garden_operations("PlantError")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        garden_operations("WaterError")
    except GardenError as e:
        print(f"Caught GardenError: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("")
    test_custom_errors()
    print("")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
