# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_finally_block.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/02 12:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/02 12:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
	def __init__(self, message: str = "Unknown garden error"):
		super().__init__(message)


class PlantError(GardenError):
	def __init__(self, message: str = "Unknown plant error"):
		super().__init__(message)


def water_plant(plant_name: str) -> None:
	if plant_name[0].isupper():
		print(f"Watering {plant_name}: [OK]")
	else:
		raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
	print("=== Garden Watering System ===")

	print("Testing valid plants...")
	try:
		print("Opening watering system")
		water_plant("Tomato")
		water_plant("Lettuce")
		water_plant("Carrots")
	finally:
		print("Closing watering system")

	print("Testing invalid plants...")
	try:
		print("Opening watering system")
		water_plant("Tomato")
		water_plant("lettuce")
	except PlantError as e:
		print(f"Caught PlantError: {e}")
		print(".. ending tests and returning to main")
	finally:
		print("Closing watering system")

	print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
	test_watering_system()
