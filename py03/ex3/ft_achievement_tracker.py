#!/usr/bin/env python3

import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    length = len(achievements)
    n = random.randint(2, length)
    player_achivements = set()

    while n > 0:
        idx = random.randint(0, length - 1)
        player_achivements.add(achievements[idx])
        n -= 1

    return player_achivements


def main() -> None:
    achievements = [
        "Crafting Genius",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
    ]

    alice = gen_player_achievements(achievements)
    bob = gen_player_achievements(achievements)
    charlie = gen_player_achievements(achievements)
    dylan = gen_player_achievements(achievements)

    distinct = alice | bob | charlie | dylan
    common = alice & bob & charlie & dylan

    only_alice = alice - (bob | charlie | dylan)
    only_bob = bob - (alice | charlie | dylan)
    only_charlie = charlie - (alice | bob | dylan)
    only_dylan = dylan - (alice | bob | charlie)

    not_alice = (bob | charlie | dylan) - (alice)
    not_bob = (alice | charlie | dylan) - (bob)
    not_charlie = (alice | bob | dylan) - (charlie)
    not_dylan = (alice | bob | charlie) - (dylan)

    print("=== Achievement Tracker System ===")
    print()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    print(f"All distinct achievements: {distinct}")
    print()
    print(f"Common achievements: {common}")
    print()
    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")
    print()
    print(f"Alice is missing: {not_alice}")
    print(f"Bob is missing: {not_bob}")
    print(f"Charlie is missing: {not_charlie}")
    print(f"Dylan is missing: {not_dylan}")


if __name__ == "__main__":
    main()
