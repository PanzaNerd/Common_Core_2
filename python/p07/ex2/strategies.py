# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    strategies.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod
from typing import cast
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class StrategyError(Exception):
	pass


class BattleStrategy(ABC):

	@abstractmethod
	def is_valid(self, creature: Creature) -> bool:
		...

	@abstractmethod
	def act(self, creature: Creature) -> None:
		...


class NormalStrategy(BattleStrategy):

	def is_valid(self, creature: Creature) -> bool:
		return True

	def act(self, creature: Creature) -> None:
		print(creature.attack())


class AggressiveStrategy(BattleStrategy):

	def is_valid(self, creature: Creature) -> bool:
		return isinstance(creature, TransformCapability)

	def act(self, creature: Creature) -> None:
		if not self.is_valid(creature):
			raise StrategyError(f"Invalid Creature '{creature.name}' for this aggressive strategy")
		transforming = cast(TransformCapability, creature)
		print(transforming.transform())
		print(creature.attack())
		print(transforming.revert())


class DefensiveStrategy(BattleStrategy):

	def is_valid(self, creature: Creature) -> bool:
		return isinstance(creature, HealCapability)

	def act(self, creature: Creature) -> None:
		if not self.is_valid(creature):
			raise StrategyError(f"Invalid Creature '{creature.name}' for this defensive strategy")
		print(creature.attack())
		healing = cast(HealCapability, creature)
		print(healing.heal())
