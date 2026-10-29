#!/usr/bin/env python3

import math


def process_coordinate(candidate: str) -> float | None:
    try:
        return float(candidate)
    except Exception as e:
        print(f"Error on parameter '{candidate}': {e}")
        return None


def get_player_pos() -> tuple[float, float, float]:
    coordinates = None

    while coordinates is None:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        splitted = raw.split(",")
        if len(splitted) != 3:
            print("Invalid syntax")
            continue
        candidates = [
            coordinate for num in splitted
            if (coordinate := process_coordinate(num)) is not None
        ]
        if len(candidates) != 3:
            continue
        coordinates = (candidates[0], candidates[1], candidates[2])

    return coordinates


def calculate_distance(coord1: tuple[float, float, float],
                       coord2: tuple[float, float, float]) -> float:
    return math.sqrt(
        (coord2[0] - coord1[0]) ** 2
        + (coord2[1] - coord1[1]) ** 2
        + (coord2[2] - coord1[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    coordinates1 = get_player_pos()
    print(f"Got a first tuple: {coordinates1}")
    print(
        f"It includes: X={coordinates1[0]:.1f}, "
        f"Y={coordinates1[1]:.1f}, Z={coordinates1[2]:.1f}"
    )
    print(
        "Distance to center: "
        f"{calculate_distance(coordinates1, (0, 0, 0)):.4f}"
    )
    print()
    print("Get a second set of coordinates")
    coordinates2 = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: "
        f"{calculate_distance(coordinates1, coordinates2):.4f}"
    )


if __name__ == "__main__":
    main()
