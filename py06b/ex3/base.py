from abc import ABC, abstractmethod


class Creature(ABC):
    name: str
    e_type: str

    def __init__(self, name: str, e_type: str) -> None:
        self.name = name
        self.e_type = e_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.e_type} type Creature"


class TransformCapability(ABC):
    transformed: bool

    def __init__(self) -> None:
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
