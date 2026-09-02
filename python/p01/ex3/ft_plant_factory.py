# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/27 21:31:15 by matthias          #+#    #+#              #
#    Updated: 2026/08/28 17:29:13 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name: str, height: float, age: int) -> None:
		self.name = name
		self.height = height
		self.age_days = age

	def grow(self) -> None:
		self.height = round(self.height + 0.8, 1)

	def age(self) -> None:
		self.age_days += 1

	def show(self) -> None:
		print(f"{self.name}: {self.height}cm, {self.age_days} days old")

if __name__ == "__main__":
	plants = [
		Plant("Rose", 25.0, 30),
		Plant("Oak", 200.0, 365),
		Plant("Cactus", 5.0, 90),
		Plant("Sunflower", 80.0, 45),
		Plant("Fern", 15.0, 120),
	]
	print("=== Plant Factory Output ===")
	for p in plants:
		print("Created:", end=" ")
		p.show()
