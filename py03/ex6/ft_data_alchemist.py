#!/usr/bin/env python3

import random


def main() -> None:
    initial_names = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]
    all_capitalized = [name.capitalize() for name in initial_names]
    only_capitalized = [
        name for name in initial_names
        if name == name.capitalize()
    ]

    scores = {name: random.randint(0, 1000) for name in all_capitalized}
    score_avg = sum([scores[name] for name in scores]) / len(scores)
    high_scores = {
        name: scores[name] for name in scores
        if scores[name] > score_avg
    }

    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {initial_names}")
    print(f"New list with all names capitalized: {all_capitalized}")
    print(f"New list of capitalized names only: {only_capitalized}")
    print()
    print(f"Score dict: {scores}")
    print(f"Score average is {score_avg:.2f}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
