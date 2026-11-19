from typing import Any
from ex3.base import Creature, TransformCapability
from .base import BattleStrategy


class NormalStrategy(BattleStrategy):

    def __init__(self):
        super().__init__("Normal")

    def is_valid(entity: Any) -> bool:
        return True

    def act(entity: Any) -> str:
        if not AggressiveStrategy.is_valid(entity):
            raise Exception("ERROR. NormalStrategy is not valid for this entity.")

        entity.attack(entity)


class AggressiveStrategy(BattleStrategy):

    def __init__(self):
        super().__init__("Aggresive")

    def is_valid(entity: Any) -> bool:
        return isinstance(entity, TransformCapability)

    def act(entity: Any) -> str:
        if not AggressiveStrategy.is_valid(entity):
            raise Exception("ERROR. AggresiveStrategy is not valid for this entity.")

        entity.transform()
        entity.attack()
        entity.revert()
