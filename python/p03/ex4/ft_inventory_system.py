# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main() -> None:
	print("=== Inventory System Analysis ===")

	inventory: dict[str, int] = {}
	for arg in sys.argv[1:]:
		parts = arg.split(":")
		if len(parts) != 2:
			print(f"Error - invalid parameter '{arg}'")
			continue
		name, qty_str = parts
		if name in inventory:
			print(f"Redundant item '{name}' - discarding")
			continue
		try:
			inventory[name] = int(qty_str)
		except ValueError as e:
			print(f"Quantity error for '{name}': {e}")

	print(f"Got inventory: {inventory}")

	names = list(inventory.keys())
	print(f"Item list: {names}")

	if len(names) == 0:
		print("Empty inventory")
		return

	total = sum(inventory.values())
	print(f"Total quantity of the {len(names)} items: {total}")

	for name in names:
		percent = inventory[name] / total * 100
		print(f"Item {name} represents {round(percent, 1)}%")

	most = names[0]
	least = names[0]
	for name in names:
		if inventory[name] > inventory[most]:
			most = name
		if inventory[name] < inventory[least]:
			least = name
	print(f"Item most abundant: {most} with quantity {inventory[most]}")
	print(f"Item least abundant: {least} with quantity {inventory[least]}")

	inventory["magic_item"] = 1
	print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
	main()
