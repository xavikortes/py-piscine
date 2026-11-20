from typing import Any

from ex3.base import TransformCapability

from .base import BattleStrategy


class NormalStrategy(BattleStrategy):

    def __init__(self) -> None:
        super().__init__("Normal")

    def is_valid(self, entity: Any) -> bool:
        return True

    def act(self, entity: Any) -> str:
        if not self.is_valid(entity):
            raise Exception(
                f"Invalid Creature '{entity.name}' for this normal strategy."
            )

        return str(entity.attack())


class AggressiveStrategy(BattleStrategy):

    def __init__(self) -> None:
        super().__init__("Aggresive")

    def is_valid(self, entity: Any) -> bool:
        return isinstance(entity, TransformCapability)

    def act(self, entity: Any) -> str:
        if not self.is_valid(entity):
            raise Exception(
                f"Invalid Creature '{entity.name}' "
                "for this aggresive strategy."
            )

        return "\n".join([
            entity.transform(),
            entity.attack(),
            entity.revert(),
        ])
