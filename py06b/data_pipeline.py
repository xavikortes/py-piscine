#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


numeric = int | float


class DataProcessor(ABC):
    name: str

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
    name = "Numeric Processor"

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
    name = "Text Processor"

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
    name = "Log Processor"

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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join([str(item) for (n, item) in data]))


class JsonPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = [f'"item_{n}": "{str(item)}"' for (n, item) in data]
        print(
            f"{{{', '.join(items)}}}"
        )


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_data(self, data: Any) -> bool:
        for proc in self.processors:
            if proc.validate(data):
                proc.ingest(data)
                return True
        return False

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            if not self.process_data(data):
                print(
                    "DataStream error - Can't process "
                    f"element in stream: {data}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if len(self.processors) == 0:
            print("No processor found, no data")
            return

        for proc in self.processors:
            rem = len(proc.storage)
            items = proc.count + rem
            print(
                f"{proc.name}: total {items} items processed, "
                f"remaining {rem} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            plugin.process_output([
                proc.output()
                for _ in range(0, nb)
                if len(proc.storage) > 0
            ])


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()
    print()
    print("Registering Processors")
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    data_stream.register_processor(num_proc)
    data_stream.register_processor(txt_proc)
    data_stream.register_processor(log_proc)
    print()
    st1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"Seend first batch of data on stream: {st1}")
    data_stream.process_stream(st1)
    print()
    data_stream.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CsvPlugin())
    print()
    data_stream.print_processors_stats()

    st2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print()
    print(f"Send another batch of data: {st2}")
    data_stream.process_stream(st2)
    print()
    data_stream.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JsonPlugin())
    print()
    data_stream.print_processors_stats()
    print()


if __name__ == "__main__":
    main()
