import sys


def print_args(args: list[str]) -> None:
    if len(args) > 0:
        print(f"Arguments received: {len(args)}")
        for (i, arg) in enumerate(args):
            print(f"Argument {i + 1}: {arg}")
    else:
        print("No arguments provided!")


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
