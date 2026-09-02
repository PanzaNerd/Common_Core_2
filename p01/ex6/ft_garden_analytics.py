# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/28 13:30:00 by matthias          #+#    #+#              #
#    Updated: 2026/08/28 13:30:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	class Stats:
		def __init__(self):
			self.grows = 0
			self.ages = 0
			self.shows = 0

		def display(self) -> None:
			print(f"Stats: {self.grows} grow, {self.ages} age, {self.shows} show")

	def __init__(self, name: str, height: float, age: int) -> None:
		self.name = name
		self._height = height
		self._age_days = age
		self.stats: "Plant.Stats" = self.Stats()

	def grow(self) -> None:
		self._height = round(self._height + 0.8, 1)
		self.stats.grows += 1

	def age(self) -> None:
		self._age_days += 1
		self.stats.ages += 1

	def show(self) -> None:
		print(f"{self.name}: {self._height}cm, {self._age_days} days old")
		self.stats.shows += 1

	@staticmethod
	def is_older_than_year(age: int) -> bool:
		return age > 365

	@classmethod
	def create_anonymous(cls):
		return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
	def __init__(self, name: str, height: float, age: int, color: str) -> None:
		super().__init__(name, height, age)
		self.color = color

	def grow(self) -> None:
		super().grow()
		self._height = round(self._height + 7.2, 1)

	def bloom(self) -> None:
		print(f"{self.name} is blooming beautifully!")

	def show(self) -> None:
		super().show()
		print(f"Color: {self.color}")


class Seed(Flower):
	def __init__(self, name: str, height: float, age: int, color: str) -> None:
		super().__init__(name, height, age, color)
		self.seeds = 0

	def grow(self) -> None:
		super().grow()
		self._height = round(self._height + 22.0, 1)

	def age(self) -> None:
		super().age()
		self._age_days += 19

	def bloom(self) -> None:
		super().bloom()
		self.seeds = 42

	def show(self) -> None:
		super().show()
		print(f"Seeds: {self.seeds}")


class Tree(Plant):
	class TreeStats(Plant.Stats):
		def __init__(self):
			super().__init__()
			self.shades = 0

		def display(self) -> None:
			super().display()
			print(f"{self.shades} shade")

	def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter
		self.stats: "Tree.TreeStats" = self.TreeStats()

	def produce_shade(self) -> None:
		print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")
		self.stats.shades += 1

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


def display_stats(plant):
	print(f"[statistics for {plant.name}]")
	plant.stats.display()


if __name__ == "__main__":
	print("=== Garden statistics ===")

	print("=== Check year-old")
	print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
	print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
	print()

	print("=== Flower")
	rose = Flower("Rose", 15.0, 10, "red")
	rose.show()
	print("Rose has not bloomed yet")
	display_stats(rose)
	print("[asking the rose to grow and bloom]")
	rose.grow()
	rose.show()
	rose.bloom()
	display_stats(rose)
	print()

	print("=== Tree")
	oak = Tree("Oak", 200.0, 365, 5.0)
	oak.show()
	display_stats(oak)
	print("[asking the oak to produce shade]")
	oak.produce_shade()
	display_stats(oak)
	print()

	print("=== Seed")
	sunflower = Seed("Sunflower", 80.0, 45, "yellow")
	sunflower.show()
	print("Sunflower has not bloomed yet")
	print("[make sunflower grow, age and bloom]")
	sunflower.grow()
	sunflower.age()
	sunflower.bloom()
	sunflower.show()
	display_stats(sunflower)
	print()

	print("=== Anonymous")
	unknown = Plant.create_anonymous()
	unknown.show()
	display_stats(unknown)
