# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    light_spellbook.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
	return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
	return f"Spell recorded: {spell_name} ({validate_ingredients(ingredients)})"
