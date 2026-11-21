#!/usr/bin/env python3

import time
from collections.abc import Callable
from functools import wraps

Spell = Callable[[str, int], str]
SpellFactory = Callable[[Spell], Spell]


def spell_timer(spell: Spell) -> Spell:
    @wraps(spell)
    def wrapper(target: str, power: int) -> str:
        print(f"Casting {spell.__name__}...")

        start = time.time()
        res = spell(target, power)
        timer = time.time() - start

        print(f"Spell completed in {timer:.3f} seconds")
        return res

    return wrapper


def power_validator(min_power: int) -> SpellFactory:
    def outer(spell: Spell) -> Spell:
        @wraps(spell)
        def inner(target: str, power: int) -> str:
            if power < min_power:
                return "Insufficient power for this spell"

            return spell(target, power)

        return inner
    return outer


def retry_spell(max_attempts: int) -> SpellFactory:
    def outer(spell: Spell) -> Spell:
        n = 0

        @wraps(spell)
        def inner(target: str, power: int) -> str:
            try:
                return spell(target, power)
            except Exception:
                nonlocal n
                n += 1
                if n < max_attempts:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {n}/{max_attempts})"
                    )
                    return inner(target, power)
                return f"Spell casting failed after {max_attempts} attempts"

        return inner
    return outer


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False

        if not all([
            letter.isalpha() or letter.isspace()
            for letter in name
        ]):
            return False

        return True

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def spell(name: str, power: int) -> str:
            return f"Successfully cast {name} with {power} power"

        return spell(spell_name, power)


def main() -> None:
    print()
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str, power: int) -> str:
        time.sleep(0.101)
        return f"Fireball attack on {target}! ({power} power)"

    print(f"Result: {fireball("Dragon", 50)}")

    print()
    print("Testing power validator...")

    @power_validator(75)
    def tornado(target: str, power: int) -> str:
        return f"Tornado spell on {target}! ({power} power)"

    print(f"Result OK: {tornado("Dragon", 80)}")
    print(f"Result KO: {tornado("Dragon", 60)}")

    print()
    print("Testing retrying spell...")

    @retry_spell(3)
    def error(target: str, power: int) -> str:
        raise Exception("Error")

    @retry_spell(3)
    def freeze(target: str, power: int) -> str:
        return f"Freezing {target}! ({power} power)"

    print(error("Dragon", 50))
    print(freeze("Dragon", 50))

    print()
    print("Testing MageGuild...")
    print(f"Gandalf: {MageGuild.validate_mage_name('Gandalf')}")
    print(f"Ga: {MageGuild.validate_mage_name('Ga')}")
    print(f"GN372: {MageGuild.validate_mage_name('GN372')}")
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fireball", 8))

    print()


if __name__ == "__main__":
    main()
