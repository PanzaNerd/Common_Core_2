# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/27 18:53:24 by matthias          #+#    #+#              #
#    Updated: 2026/08/27 21:25:13 by matthias         ###   ########.fr        #
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
	rose = Plant("Rose", 25, 30)
	print("=== Garden Plant Growth ===")
	rose.show()
	for day in range(1, 8):
		rose.grow()
		rose.age()
		print(f"=== Day {day} ===")
		rose.show()
	print(f"Growth this week: {round(rose.height - 25, 1)}cm")
