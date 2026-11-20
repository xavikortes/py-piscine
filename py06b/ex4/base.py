from abc import ABC, abstractmethod

from ex3.base import Creature


class BattleStrategy(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass
