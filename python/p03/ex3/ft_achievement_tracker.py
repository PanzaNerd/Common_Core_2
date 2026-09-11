# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: matthias <matthias@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by matthias          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by matthias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

ACHIEVEMENTS = [
	"Crafting Genius", "World Savior", "Master Explorer", "Collector Supreme",
	"Untouchable", "Boss Slayer", "Strategist", "Unstoppable",
	"Speed Runner", "Survivor", "Treasure Hunter", "First Steps",
	"Sharp Mind", "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
	n = random.randint(6, 9)
	return set(random.sample(ACHIEVEMENTS, n))


def main() -> None:
	print("=== Achievement Tracker System ===")

	players = {
		"Alice": gen_player_achievements(),
		"Bob": gen_player_achievements(),
		"Charlie": gen_player_achievements(),
		"Dylan": gen_player_achievements(),
	}

	for name in players:
		print(f"Player {name}: {players[name]}")

	all_distinct: set[str] = set()
	for name in players:
		all_distinct = all_distinct.union(players[name])
	print(f"All distinct achievements: {all_distinct}")

	common = set(ACHIEVEMENTS)
	for name in players:
		common = common.intersection(players[name])
	print(f"Common achievements: {common}")

	for name in players:
		others: set[str] = set()
		for other in players:
			if other != name:
				others = others.union(players[other])
		only = players[name].difference(others)
		print(f"Only {name} has: {only}")

	for name in players:
		missing = set(ACHIEVEMENTS).difference(players[name])
		print(f"{name} is missing: {missing}")


if __name__ == "__main__":
	main()
