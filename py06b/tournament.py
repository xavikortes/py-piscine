#!/usr/bin/env python3

from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import BattleStrategy, NormalStrategy, AggressiveStrategy


def battle(
    ent1: tuple[CreatureFactory, BattleStrategy],
    ent2: tuple[CreatureFactory, BattleStrategy]
) -> None:
    print(ent1.describe())
    print(" vs.")
    print(ent2.describe())
    print(" now fight!")
    print(ent1.attack())
    print(ent2.attack())


def tournament(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print(f" {[f'({creat.name}+{strat.name})' for (creat, strat) in opponents]}")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    for opp1 in opponents:
        for opp2 in opponents:
            if opp1 == opp2:
                continue

            print("* Battle *")
            battle(opp1, opp2)


def main() -> None:
    flame_fact = FlameFactory()
    trans_fact = TransformCreatureFactory()

    norm_strat = NormalStrategy()
    aggr_strat = AggressiveStrategy()

    print("Tournament 0 (basic)")
    opps0 = [
        (flame_fact, norm_strat),
        (trans_fact, aggr_strat),
    ]
    tournament(opps0)

    print("Tournament 1 (error)")
    opps1 = []
    tournament(opps1)


if __name__ == "__main__":
    main()
