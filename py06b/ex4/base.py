from abc import ABC, abstractmethod
from typing import Any


class BattleStrategy(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def act(self, entity: Any) -> str:
        pass

    @abstractmethod
    def is_valid(self, entity: Any) -> bool:
        pass
