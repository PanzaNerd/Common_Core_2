# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    potions.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from alchemy.elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
	return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"


def strength_potion() -> str:
	return f"Strength potion brewed with '{create_fire()}' and '{create_water()}'"
