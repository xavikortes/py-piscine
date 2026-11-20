#!/usr/bin/env python3

from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import AggressiveStrategy, BattleStrategy, NormalStrategy


def battle(
    ent1: tuple[CreatureFactory, BattleStrategy],
    ent2: tuple[CreatureFactory, BattleStrategy]
) -> bool:
    print("* Battle *")

    fact1, strat1 = ent1
    creat1 = fact1.create_base()
    print(creat1.describe())
    print(" vs.")

    fact2, strat2 = ent2
    creat2 = fact2.create_base()
    print(creat2.describe())
    print(" now fight!")

    try:
        print(strat1.act(creat1))
        print(strat2.act(creat2))
        print()
    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")
        print()
        return False

    return True


def tournament(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    for i in range(0, len(opponents)):
        opp1 = opponents[i]
        for j in range(i + 1, len(opponents)):
            opp2 = opponents[j]

            if not battle(opp1, opp2):
                return


def main() -> None:
    flame_fact = FlameFactory()
    trans_fact = TransformCreatureFactory()

    norm_strat = NormalStrategy()
    aggr_strat = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Shiftling+Aggresive) ]")
    opps0: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame_fact, norm_strat),
        (trans_fact, aggr_strat),
    ]
    tournament(opps0)

    print("Tournament 1 (error)")
    print(" [ (Shiftling+Aggresive), (Flameling+Aggresive) ]")
    opps1: list[tuple[CreatureFactory, BattleStrategy]] = [
        (trans_fact, aggr_strat),
        (flame_fact, aggr_strat),
    ]
    tournament(opps1)


if __name__ == "__main__":
    main()
