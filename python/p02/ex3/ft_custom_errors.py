# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/02 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/02 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
	def __init__(self, message: str = "Unknown garden error"):
		super().__init__(message)


class PlantError(GardenError):
	def __init__(self, message: str = "Unknown plant error"):
		super().__init__(message)


class WaterError(GardenError):
	def __init__(self, message: str = "Unknown water error"):
		super().__init__(message)


def test_custom_errors() -> None:
	print("=== Custom Garden Errors Demo ===")

	print("Testing PlantError...")
	try:
		raise PlantError("The tomato plant is wilting!")
	except PlantError as e:
		print(f"Caught PlantError: {e}")

	print("Testing WaterError...")
	try:
		raise WaterError("Not enough water in the tank!")
	except WaterError as e:
		print(f"Caught WaterError: {e}")

	print("Testing catching all garden errors...")
	try:
		raise PlantError("The tomato plant is wilting!")
	except GardenError as e:
		print(f"Caught GardenError: {e}")

	try:
		raise WaterError("Not enough water in the tank!")
	except GardenError as e:
		print(f"Caught GardenError: {e}")

	print("All custom error types work correctly!")


if __name__ == "__main__":
	test_custom_errors()
