# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capacitor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
	print("Testing Creature with healing capability")
	print("base:")
	sproutling = HealingCreatureFactory().create_base()
	print(sproutling.describe())
	print(sproutling.attack())
	print(sproutling.heal())
	print("evolved:")
	bloomelle = HealingCreatureFactory().create_evolved()
	print(bloomelle.describe())
	print(bloomelle.attack())
	print(bloomelle.heal())

	print("Testing Creature with transform capability")
	print("base:")
	shiftling = TransformCreatureFactory().create_base()
	print(shiftling.describe())
	print(shiftling.attack())
	print(shiftling.transform())
	print(shiftling.attack())
	print(shiftling.revert())
	print("evolved:")
	morphagon = TransformCreatureFactory().create_evolved()
	print(morphagon.describe())
	print(morphagon.attack())
	print(morphagon.transform())
	print(morphagon.attack())
	print(morphagon.revert())


if __name__ == "__main__":
	main()
