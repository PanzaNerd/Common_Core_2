# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capabilities.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod


class HealCapability(ABC):

	@abstractmethod
	def heal(self) -> str:
		...


class TransformCapability(ABC):

	def __init__(self) -> None:
		self._transformed = False

	@abstractmethod
	def transform(self) -> str:
		...

	@abstractmethod
	def revert(self) -> str:
		...
