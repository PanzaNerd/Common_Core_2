import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as floats "
                           "in format 'x,y,z': ")
        pieces = user_input.split(",")
        if len(pieces) != 3:
            print("Invalid syntax")
            continue
        numbers = []
        all_valid = True
        for piece in pieces:
            try:
                numbers.append(float(piece))
            except ValueError as e:
                print(f"Error on parameter '{piece}': {e}")
                all_valid = False
                break
        if all_valid:
            return (numbers[0], numbers[1], numbers[2])


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    x1, y1, z1 = get_player_pos()
    print(f"Got a first tuple: {(x1, y1, z1)}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    distance = math.sqrt(x1 * x1 + y1 * y1 + z1 * z1)
    print(f"Distance to center: {round(distance, 4)}")

    print("Get a second set of coordinates")
    x2, y2, z2 = get_player_pos()

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    main()
