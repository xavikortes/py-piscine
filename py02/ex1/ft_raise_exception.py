#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}ºC is too cold for plants (min 0ºC)")
    if temp > 40:
        raise ValueError(f"{temp}ºC is too hot for plants (max 40ºC)")
    return temp


def test_temperature() -> None:
    tests = [
        "25",
        "abc",
        "100",
        "-50",
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
    print("=== Garden Temperature Checker ===")
    print("")
    test_temperature()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
