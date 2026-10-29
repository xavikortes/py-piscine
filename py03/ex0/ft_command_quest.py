#!/usr/bin/env python3

import sys


def print_args(args: list[str]) -> None:
    if len(args) == 0:
        print("No arguments provided!")
        return
    print(f"Arguments received: {len(args)}")
    i = 0
    while i < len(args):
        print(f"Argument {i + 1}: {args[i]}")
        i += 1


def main() -> None:
    args = sys.argv
    program_name = args[0]
    argc = len(args)

    print("=== Command Quest ===")
    print(f"Program name: {program_name}")
    print_args(args[1:])
    print(f"Total arguments: {argc}")
    print()


if __name__ == "__main__":
    main()
