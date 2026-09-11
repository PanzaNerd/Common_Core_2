# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dark_spellbook.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
	return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
	return f"Spell recorded: {spell_name} ({dark_validate_ingredients(ingredients)})"
