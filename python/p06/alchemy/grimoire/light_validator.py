# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    light_validator.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ALLOWED = ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
	lower = ingredients.lower()
	for word in ALLOWED:
		if word in lower:
			return f"{ingredients} - VALID"
	return f"{ingredients} - INVALID"
