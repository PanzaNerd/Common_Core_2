# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tournament.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ex0 import AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0.factories import CreatureFactory
from ex2 import AggressiveStrategy, BattleStrategy, DefensiveStrategy, NormalStrategy, StrategyError


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
	print("*** Tournament ***")
	print(f"{len(opponents)} opponents involved")
	creatures = []
	for factory, strategy in opponents:
		creatures.append((factory.create_base(), strategy))
	for i in range(len(creatures)):
		for j in range(i + 1, len(creatures)):
			a, strat_a = creatures[i]
			b, strat_b = creatures[j]
			print("* Battle *")
			print(a.describe())
			print("vs.")
			print(b.describe())
			print("now fight!")
			try:
				strat_a.act(a)
				strat_b.act(b)
			except StrategyError as e:
				print(f"Battle error, aborting tournament: {e}")
				return


def main() -> None:
	print("Tournament 0 (basic)")
	print("[ (Flameling+Normal), (Healing+Defensive) ]")
	battle([(FlameFactory(), NormalStrategy()), (HealingCreatureFactory(), DefensiveStrategy())])

	print("Tournament 1 (error)")
	print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
	battle([(FlameFactory(), AggressiveStrategy()), (HealingCreatureFactory(), DefensiveStrategy())])

	print("Tournament 2 (multiple)")
	print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
	battle([
		(AquaFactory(), NormalStrategy()),
		(HealingCreatureFactory(), DefensiveStrategy()),
		(TransformCreatureFactory(), AggressiveStrategy()),
	])


if __name__ == "__main__":
	main()
