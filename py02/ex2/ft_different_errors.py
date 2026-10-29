#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    match (operation_number):
        case 0:
            int("abc")
        case 1:
            1 / 0
        case 2:
            open("/non/existent/file")
        case 3:
            "7" + 5  # type: ignore


def test_error_types() -> None:
    i = 0
    while i < 5:
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed succesfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        i += 1


def main() -> None:
    print("=== Garden Error Types Demo ===")
    print("")
    test_error_types()
    print("")
    print("All error types tested succesfully!")


if __name__ == "__main__":
    main()
