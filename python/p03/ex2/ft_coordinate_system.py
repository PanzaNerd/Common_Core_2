# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import math


def get_player_pos() -> tuple[float, float, float]:
	while True:
		raw = input("Enter new coordinates as floats in format 'x,y,z': ")
		parts = raw.split(",")
		if len(parts) != 3:
			print("Invalid syntax")
			continue
		values = []
		ok = True
		for part in parts:
			try:
				values.append(float(part))
			except ValueError as e:
				print(f"Error on parameter '{part}': {e}")
				ok = False
				break
		if ok:
			return (values[0], values[1], values[2])


def main() -> None:
	print("=== Game Coordinate System ===")
	print("Get a first set of coordinates")
	x1, y1, z1 = get_player_pos()
	print(f"Got a first tuple: {(x1, y1, z1)}")
	print(f"It includes: X={x1}, Y={y1}, Z={z1}")
	d = math.sqrt(x1 * x1 + y1 * y1 + z1 * z1)
	print(f"Distance to center: {round(d, 4)}")

	print("Get a second set of coordinates")
	x2, y2, z2 = get_player_pos()
	d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
	print(f"Distance between the 2 sets of coordinates: {round(d, 4)}")


if __name__ == "__main__":
	main()
