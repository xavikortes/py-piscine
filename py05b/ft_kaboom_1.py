#!/usr/bin/env python3

def main() -> None:
    print("=== Kaboom 1 ===")
    print("Using alchemy/grimoire/dark_spellbook.py directly")
    print("Testing import now: THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    from alchemy.grimoire import dark_spellbook

    print(dark_spellbook.dark_spell_record("Fantasy", "Earth, wind and fire"))
    print()


if __name__ == "__main__":
    main()
