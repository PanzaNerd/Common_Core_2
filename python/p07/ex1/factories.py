# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    factories.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ex0.factories import CreatureFactory
from .creatures import Bloomelle, Morphagon, Shiftling, Sproutling


class HealingCreatureFactory(CreatureFactory):

	def create_base(self):
		return Sproutling()

	def create_evolved(self):
		return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

	def create_base(self):
		return Shiftling()

	def create_evolved(self):
		return Morphagon()
