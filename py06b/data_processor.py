#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


numeric = int | float


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.storage: list[Any] = []
        self.count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self.storage) == 0:
            return (-1, "[Error] No values left.")

        self.count += 1
        return (self.count - 1, self.storage.pop(0))


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all([self.validate(item) for item in data])

        if isinstance(data, numeric):
            return True

        return False

    def ingest(self, data: numeric | list[numeric]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if not isinstance(data, list):
            self.storage.append(data)
            return

        for item in data:
            self.ingest(item)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all([self.validate(item) for item in data])

        if isinstance(data, str):
            return True

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if not isinstance(data, list):
            self.storage.append(data)
            return

        for item in data:
            self.ingest(item)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all([self.validate(item) for item in data])

        if not isinstance(data, dict):
            return False

        keys = data.keys()
        if len(keys) != 2:
            return False

        if "log_level" not in keys:
            return False
        if "log_message" not in keys:
            return False

        values = data.values()
        for value in values:
            if not isinstance(value, str):
                return False

        return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        if not isinstance(data, list):
            self.storage.append(f"{data['log_level']}: {data['log_message']}")
            return

        for item in data:
            self.ingest(item)


def main() -> None:
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    print("=== Code Nexus - Data Processor ===")

    print()
    print("Testing Numeric Processor...")

    print()
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    print(
        " Trying to validate input '[1, 2, 3]': "
        f"{num_proc.validate([1, 2, 3])}"
    )
    print(
        " Trying to validate input '[1, a, 3]': "
        f"{num_proc.validate([1, 'a', 3])}"
    )

    print()
    print(" Test invalid ingestion of string 'foo' without validation:")
    try:
        num_proc.ingest('foo')  # type: ignore
    except Exception as e:
        print(f" Got exception: {e}")

    print(" Processing data: '[1, 2, 3, 4, 5]'")
    num_proc.ingest([1, 2, 3, 4, 5])

    print()
    print(" Extracting 3 values...")
    for _ in range(0, 3):
        idx, val = num_proc.output()
        print(f" Numeric value {idx}: {val}")
    print()

    print()
    print("Testing Text Processor...")

    print()
    print(f" Trying to validate input '42': {text_proc.validate(42)}")
    print(
        " Trying to validate input 'Hello Nexus World': "
        f"{text_proc.validate('Hello Nexus World')}"
    )
    print(
        " Trying to validate input '[Hello, Nexus, World]': "
        f"{text_proc.validate(['Hello', 'Nexus', 'World'])}"
    )
    print(
        " Trying to validate input '[Hello, 42, World]': "
        f"{text_proc.validate(['Hello', 42, 'World'])}"
    )

    print()
    print(" Test invalid ingestion of number '42' without validation:")
    try:
        text_proc.ingest(42)  # type: ignore
    except Exception as e:
        print(f" Got exception: {e}")

    print(" Processing data: '[Hello, Nexus, World]'")
    text_proc.ingest(['Hello', 'Nexus', 'World'])

    print()
    print(" Extracting 1 value...")
    idx, val = text_proc.output()
    print(f" Text value {idx}: {val}")
    print()

    print()
    print("Testing Log Processor...")

    print()
    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    print(
        " Trying to validate input '{Hello: World}': "
        f"{log_proc.validate({'Hello': 'World'})}"
    )
    dict_ok = {'log_level': 'DEBUG', 'log_message': 'Debugging...'}
    print(
        " Trying to validate input "
        f"'{{'log_level': 'DEBUG', 'log_message': 'Debugging...'}}'"
        f": {log_proc.validate(dict_ok)}"
    )
    dict_ko = {'log_level': 42, 'log_message': 'Debugging...'}
    print(
        " Trying to validate input "
        f"'{{'log_level': 42, 'log_message': 'Debugging...'}}': "
        f"{log_proc.validate(dict_ko)}"
    )

    print()
    print(" Test invalid ingestion of number '42' without validation:")
    try:
        log_proc.ingest(42)  # type: ignore
    except Exception as e:
        print(f" Got exception: {e}")

    print(
        " Processing data: '[{'log_level': 'NOTICE', 'log_message': "
        "'Connection to server'}, {'log_level': 'ERROR', 'log_message'"
        ": 'Unauthorized access!!'}]'"
    )
    log_proc.ingest([
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ])

    print()
    print(" Extracting 2 values...")
    for _ in range(0, 2):
        idx, val = log_proc.output()
        print(f" Log entry {idx}: {val}")
    print()


if __name__ == "__main__":
    main()
