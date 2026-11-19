#!/usr/bin/env python3

from ex3 import TransformCreatureFactory


def main() -> None:
    trans_fact = TransformCreatureFactory()
    base = trans_fact.create_base()
    evolved = trans_fact.create_evolved()

    print("Testing Creature with transform factory")
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    main()
