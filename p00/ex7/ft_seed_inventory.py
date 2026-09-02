# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/27 14:30:59 by matthias          #+#    #+#              #
#    Updated: 2026/08/27 14:43:39 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	name = seed_type.capitalize()
	if unit == "packets":
		print(f"{name} seeds: {quantity} packets available")
	elif unit == "grams":
		print(f"{name} seeds: {quantity} grams total")
	elif unit == "area":
		print(f"{name} seeds: covers {quantity} square meters")
	else:
		print("Unknown unit type")

#ft_seed_inventory("tomato", 15, "packets")
#ft_seed_inventory("carrot", 8, "grams")
#ft_seed_inventory("lettuce", 12, "area")
#ft_seed_inventory("tomato", 15, "liters")
