from ex3.base import Creature, TransformCapability

from .base import BattleStrategy


class NormalStrategy(BattleStrategy):

    def __init__(self) -> None:
        super().__init__("Normal")

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' for this normal strategy."
            )

        return str(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def __init__(self) -> None:
        super().__init__("Aggresive")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not isinstance(creature, TransformCapability):
            raise Exception(
                f"Invalid Creature '{creature.name}' "
                "for this aggresive strategy."
            )

        return "\n".join([
            creature.transform(),
            creature.attack(),
            creature.revert(),
        ])
