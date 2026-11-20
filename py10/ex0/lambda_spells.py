#!/usr/bin/env python3

from typing import TypedDict

Artifact = TypedDict('Artifact', {
    "name": str,
    "power": int,
    "type": str,
})
Mage = TypedDict('Mage', {
    "name": str,
    "power": int,
    "element": str,
})
Stats = TypedDict('Stats', {
    "max_power": int,
    "min_power": int,
    "avg_power": float,
})


def artifact_sorter(artifacts: list[Artifact]) -> list[Artifact]:
    return sorted(artifacts, key=lambda art: art["power"], reverse=True)


def power_filter(mages: list[Mage], min_power: int) -> list[Mage]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[Mage]) -> Stats:
    if len(mages) == 0:
        return {
            "max_power": 0,
            "min_power": 0,
            "avg_power": round(0, 2),
        }

    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(
            sum(map(lambda mage: mage["power"], mages)) / len(mages),
            2
        ),
    }


def main() -> None:
    artifacts: list[Artifact] = [
        {
            "name": "Crystal Orb",
            "power": 77,
            "type": "relic",
        },
        {
            "name": "Storm Crown",
            "power": 62,
            "type": "accesory",
        },
        {
            "name": "Lightning Rod",
            "power": 83,
            "type": "focus",
        },
        {
            "name": "Fire Staff",
            "power": 120,
            "type": "weapon",
        }
    ]

    mages: list[Mage] = [
        {
            "name": "Luna",
            "power": 75,
            "element": "wind",
        },
        {
            "name": "Phoenix",
            "power": 51,
            "element": "fire",
        },
        {
            "name": "Morgan",
            "power": 67,
            "element": "shadow",
        },
        {
            "name": "Jordan",
            "power": 98,
            "element": "earth",
        }
    ]

    spells = [
        "fireball",
        "shield",
        "freeze",
        "meteor",
    ]

    print()
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for artifact in sorted_artifacts:
        print(f" - {artifact["name"]} ({artifact["power"]} power)")

    print()
    print("Testing power filter...")
    filtered_mages = power_filter(mages, 70)
    for mage in filtered_mages:
        print(f" - {mage["name"]} ({mage["power"]} power)")

    print()
    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells)
    for spell in transformed_spells:
        print(f" - {spell}")

    print()
    print("Testing mage stats...")
    stats = mage_stats(mages)
    for k, v in stats.items():
        print(f" - {k}: {v}")

    print()


if __name__ == "__main__":
    main()
