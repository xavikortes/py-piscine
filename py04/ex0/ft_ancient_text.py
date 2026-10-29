#!/usr/bin/env python3

import sys
import typing


def get_file(filename: str) -> typing.IO[str] | None:
    print(f"Accessing file '{filename}'")
    try:
        return open(filename, mode="r")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        print()
    return None


def print_content(content: str) -> None:
    print("---")
    print()
    print(content)
    print("---")


def main() -> None:
    program_name = sys.argv[0]
    argc = len(sys.argv)

    if argc != 2:
        print(f"Usage: {program_name} <file>")
        print()
        return

    print("=== Cyber Archives Recovery ===")

    filename = sys.argv[1]
    file = get_file(filename)
    if file is None:
        return

    content = file.read()
    print_content(content)
    file.close()
    print(f"File '{filename}' closed.")
    print()


if __name__ == "__main__":
    main()
