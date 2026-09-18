def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    print("Input data is '25'")
    temperature = input_temperature("25")
    print(f"Temperature is now {temperature}°C")

    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
