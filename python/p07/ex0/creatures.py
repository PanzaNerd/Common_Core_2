# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    creatures.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod


class Creature(ABC):

	def __init__(self, name: str, creature_type: str) -> None:
		self.name = name
		self.creature_type = creature_type

	@abstractmethod
	def attack(self) -> str:
		...

	def describe(self) -> str:
		return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):

	def __init__(self) -> None:
		super().__init__("Flameling", "Fire")

	def attack(self) -> str:
		return "Flameling uses Ember!"


class Pyrodon(Creature):

	def __init__(self) -> None:
		super().__init__("Pyrodon", "Fire/Flying")

	def attack(self) -> str:
		return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):

	def __init__(self) -> None:
		super().__init__("Aquabub", "Water")

	def attack(self) -> str:
		return "Aquabub uses Water Gun!"


class Torragon(Creature):

	def __init__(self) -> None:
		super().__init__("Torragon", "Water")

	def attack(self) -> str:
		return "Torragon uses Hydro Pump!"
