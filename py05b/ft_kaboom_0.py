#!/usr/bin/env python3

from alchemy import grimoire


def main() -> None:
    light_spell = grimoire.light_spell_record("Fantasy", "Earth, wind and fire")

    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record light spell: {light_spell}")
    print()


if __name__ == "__main__":
    main()
