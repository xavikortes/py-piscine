#!/usr/bin/env python3

from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul
from typing import Any

Enchantment = Callable[[int, str, str], str]
PartialEnchantment = Callable[[str], str]


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0

    match operation:
        case "add":
            return reduce(add, spells, 0)
        case "multiply":
            return reduce(mul, spells, 1)
        case "max":
            return max(spells)
        case "min":
            return min(spells)
        case _:
            raise ValueError(f"Operation {operation} not supported.")


def partial_enchanter(
    base_enchantment: Enchantment
) -> dict[str, PartialEnchantment]:

    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "water": partial(base_enchantment, 50, "water"),
    }


@lru_cache()
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n can't be negative")
    if n <= 1:
        return n

    return memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(power: int) -> str:
        return f"{power} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return spell

    @dispatch.register(list)
    def _(lst: list[Any]) -> str:
        return f"{len(lst)} spells"

    return dispatch


def main() -> None:
    print()
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]

    print(f" - Sum: {spell_reducer(spells, "add")}")
    print(f" - Product: {spell_reducer(spells, "multiply")}")
    print(f" - Max: {spell_reducer(spells, "max")}")
    print(f" - Min: {spell_reducer(spells, "min")}")

    print()
    print("Testing partial enchanter...")

    def enchantment(power: int, element: str, target: str) -> str:
        return f"Attack {target} with {element} ({power} power)"

    partials = partial_enchanter(enchantment)

    for k, fun in partials.items():
        print(f" - {k.capitalize()}: {fun("Dragon")}")

    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print()
    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher("fireball")}")
    print(f"Multi-cast: {dispatcher([1, 2, 3])}")
    print(dispatcher(7.2))

    print()


if __name__ == "__main__":
    main()
