from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def act() -> str:
        pass

    @abstractmethod
    def is_valid() -> bool:
        pass