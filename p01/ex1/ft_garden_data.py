# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/27 18:21:32 by matthias          #+#    #+#              #
#    Updated: 2026/08/27 18:37:16 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
	def __init__(self, name: str, height: float, age: int) -> None:
		self.name = name
		self.height = height
		self.age = age

	def show(self) -> None:
		print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
	rose = Plant("Rose", 25, 30)
	sunflower = Plant("Sunflower", 80, 45)
	cactus = Plant("Cactus", 15, 120)

	print("=== Garden Plant Registry ===")
	rose.show()
	sunflower.show()
	cactus.show()
