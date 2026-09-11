# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipes.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from elements import create_fire
from alchemy.elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
	return f"Recipe transmuting Lead to Gold: brew '{create_air()}' and '{strength_potion()}' mixed with '{create_fire()}'"
