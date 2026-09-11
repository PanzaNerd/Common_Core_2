# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    factories.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod
from .creatures import Aquabub, Creature, Flameling, Pyrodon, Torragon


class CreatureFactory(ABC):

	@abstractmethod
	def create_base(self) -> Creature:
		...

	@abstractmethod
	def create_evolved(self) -> Creature:
		...


class FlameFactory(CreatureFactory):

	def create_base(self) -> Creature:
		return Flameling()

	def create_evolved(self) -> Creature:
		return Pyrodon()


class AquaFactory(CreatureFactory):

	def create_base(self) -> Creature:
		return Aquabub()

	def create_evolved(self) -> Creature:
		return Torragon()
