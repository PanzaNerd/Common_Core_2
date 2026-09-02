# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/28 13:10:00 by matthias          #+#    #+#              #
#    Updated: 2026/08/28 18:37:53 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name: str, height: float, age: int) -> None:
		self.name = name
		self._height = height
		self._age_days = age

	def grow(self) -> None:
		self._height = round(self._height + 0.8, 1)

	def age(self) -> None:
		self._age_days += 1

	def show(self) -> None:
		print(f"{self.name}: {self._height}cm, {self._age_days} days old")


class Flower(Plant):
	def __init__(self, name: str, height: float, age: int, color: str) -> None:
		super().__init__(name, height, age)
		self.color = color

	def bloom(self) -> None:
		print(f"{self.name} is blooming beautifully!")

	def show(self) -> None:
		super().show()
		print(f"Color: {self.color}")


class Tree(Plant):
	def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter

	def produce_shade(self) -> None:
		print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")

	def show(self) -> None:
		super().show()
		print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
	def __init__(self, name: str, height: float, age: int, harvest_season: str) -> None:
		super().__init__(name, height, age)
		self.harvest_season = harvest_season
		self.nutritional_value = 0

	def grow(self) -> None:
		super().grow()
		self._height = round(self._height + 1.3, 1)

	def age(self) -> None:
		super().age()
		self.nutritional_value += 1

	def show(self) -> None:
		super().show()
		print(f"Harvest season: {self.harvest_season}")
		print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
	print("=== Garden Plant Types ===")

	print("=== Flower")
	rose = Flower("Rose", 15.0, 10, "red")
	rose.show()
	print("Rose has not bloomed yet")
	print("[asking the rose to bloom]")
	rose.bloom()
	print()

	print("=== Tree")
	oak = Tree("Oak", 200.0, 365, 5.0)
	oak.show()
	print("[asking the oak to produce shade]")
	oak.produce_shade()
	print()

	print("=== Vegetable")
	tomato = Vegetable("Tomato", 5.0, 10, "April")
	tomato.show()
	print("[make tomato grow and age for 20 days]")
	for _ in range(20):
		tomato.grow()
		tomato.age()
	tomato.show()
