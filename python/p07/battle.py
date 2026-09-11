# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    battle.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ex0 import AquaFactory, FlameFactory
from ex0.factories import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
	print("Testing factory")
	base = factory.create_base()
	evolved = factory.create_evolved()
	print(base.describe())
	print(base.attack())
	print(evolved.describe())
	print(evolved.attack())


def test_battle(factory_a: CreatureFactory, factory_b: CreatureFactory) -> None:
	a = factory_a.create_base()
	b = factory_b.create_base()
	print("Testing battle")
	print(a.describe())
	print("vs.")
	print(b.describe())
	print("fight!")
	print(a.attack())
	print(b.attack())


def main() -> None:
	test_factory(FlameFactory())
	test_factory(AquaFactory())
	test_battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
	main()
