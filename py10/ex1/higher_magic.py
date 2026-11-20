from collections.abc import Callable

Spell = Callable[[str, int], str]
CombinedSpell = Callable[[str, int], tuple[str, str]]
SpellCondition = Callable[[str, int], bool]
SpellList = Callable[[str, int], list[str]]


def spell_combiner(spell1: Spell, spell2: Spell) -> CombinedSpell:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (
            spell1(target, power),
            spell2(target, power)
        )
    return combined_spell


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: SpellCondition, spell: Spell) -> Spell:
    def conditioned_spell(target: str, power: int) -> str:
        if not condition(target, power):
            return "Spell fizzled"
        return spell(target, power)
    return conditioned_spell


def spell_sequence(spells: list[Spell]) -> SpellList:
    def sequenced_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequenced_spell


def main() -> None:
    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} power"

    def shield(target: str, power: int) -> str:
        return f"Shield protects {target} for {power} turns"

    def darkness(target: str, power: int) -> str:
        return f"Darkness blinds {target} for {power} turns"

    print()
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, darkness)
    print(combined("Dragon", 30))

    print()
    print("Testing power amplifier...")
    print(f"Original: {fireball('Dragon', 10)}")
    amplified = power_amplifier(fireball, 5)
    print(f"Amplified: {amplified('Dragon', 10)}")

    print()
    print("Testing conditional caster...")
    condicional = conditional_caster(lambda s, p: p > 20, heal)
    print(f"Condicional KO: {condicional('Dragon', 10)}")
    print(f"Condicional OK: {condicional('Dragon', 30)}")

    print()
    print("Testing spell sequence...")
    spells: list[Spell] = [
        fireball, heal, shield, darkness
    ]
    sequence = spell_sequence(spells)
    for cast in sequence('Dragon', 15):
        print(f" - {cast}")
    print()


if __name__ == "__main__":
    main()
