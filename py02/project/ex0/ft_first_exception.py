def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    tests = [
        "25",
        "abc",
    ]
    for test in tests:
        try:
            print(f"Input data is '{test}'")
            input_temperature(test)
            print(f"Temperature is now {test}ºC")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print("")


def main() -> None:
    print("=== Garden Temperature ===")
    print("")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
