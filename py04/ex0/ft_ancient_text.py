#!/usr/bin/env python3

import sys


def print_file_content(filename: str) -> None:
    f = None
    try:
        print(f"Accessing file '{filename}'")
        f = open(filename, mode="r")
        print("---")
        print()
        print(f.read())
        print()
        print("---")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if f is not None:
            f.close()
            print(f"File '{filename}' closed.")


def main() -> None:
    program_name = sys.argv[0]
    argc = len(sys.argv)

    if argc != 2:
        print(f"Usage: {program_name} <file>")
        print()
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print_file_content(filename)
    print()


if __name__ == "__main__":
    main()
