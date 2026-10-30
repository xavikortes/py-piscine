#!/usr/bin/env python3

import sys
import typing


def print_error(msg: str) -> None:
    print(f"[STDERR] {msg}", file=sys.stderr)


def get_file(filename: str, mode: str) -> typing.IO[str] | None:
    try:
        return open(filename, mode=mode)
    except Exception as e:
        print_error(f"Error opening file '{filename}': {e}")
        print()
    return None


def print_content(content: str) -> None:
    print("---")
    print()
    print(content)
    print("---")


def save_content(content: str) -> None:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    filename = sys.stdin.readline()
    filename = filename.rstrip()
    if not filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{filename}'")
    f = get_file(filename, "w")
    if f is None:
        print("Data not saved.")
        return
    f.write(content)
    f.close()
    print(f"Data saved in '{filename}'.")


def main() -> None:
    program_name = sys.argv[0]
    argc = len(sys.argv)

    if argc != 2:
        print(f"Usage: {program_name} <file>")
        print()
        return

    print("=== Cyber Archives Recovery & Preservation ===")

    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")
    file = get_file(filename, "r")
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
