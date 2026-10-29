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


def save_content(content: str) -> None:
    filename = input("Enter new file name (or empty): ")
    if not filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{filename}'")
    f = open(filename, "w")
    f.write(content)
    f.close()
    print(f"Data saved in '{filename}.'")


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

    new_content = content.replace("\n", "#\n")
    print()
    print("Transform data:")
    print_content(new_content)
    save_content(new_content)
    print()


if __name__ == "__main__":
    main()
