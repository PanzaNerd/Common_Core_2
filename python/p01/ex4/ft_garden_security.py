# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/28 12:40:18 by matthias          #+#    #+#              #
#    Updated: 2026/08/28 18:37:13 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name: str, height: float, age: int) -> None:
		self.name = name
		self._height = height
		self._age = age

	def get_height(self) -> float:
		return self._height

	def get_age(self) -> int:
		return self._age

	def set_height(self, new_height: float) -> None:
		if new_height < 0:
			print(f"{self.name}: Error, height can't be negative")
		else:
			self._height = new_height

	def set_age(self, new_age: int) -> None:
		if new_age < 0:
			print(f"{self.name}: Error, age can't be negative")
		else:
			self._age = new_age

	def show(self) -> None:
		print(f"{self.name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
	rose = Plant("Rose", 15.0, 10)
	print("=== Garden Security System ===")
	print("Plant created:", end=" ")
	rose.show()
	print()

	rose.set_height(25.0)
	print("Height updated: 25cm")
	rose.set_age(30)
	print("Age updated: 30 days")
	print()

	rose.set_height(-5)
	print("Height update rejected")
	rose.set_age(-10)
	print("Age update rejected")
	print()

	print("Current state:", end=" ")
	rose.show()
