#!/usr/bin/env python3

from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing factory")
    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def battle(fact1: CreatureFactory, fact2: CreatureFactory) -> None:
    base1 = fact1.create_base()
    base2 = fact2.create_base()

    print("Testing battle")
    print(base1.describe())
    print(" vs.")
    print(base2.describe())
    print(" fight!")
    print(base1.attack())
    print(base2.attack())


def main() -> None:
    flame_fact = FlameFactory()
    trans_fact = TransformCreatureFactory()

    test_factory(flame_fact)
    print()
    test_factory(trans_fact)
    print()
    battle(flame_fact, trans_fact)


if __name__ == "__main__":
    main()
