# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by mpanzani         ###   ########.fr        #
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
	n = random.randint(8, 11)
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

	all_achievements: set[str] = set()
	for name in players:
		all_achievements = all_achievements.union(players[name])
	print(f"All distinct achievements: {all_achievements}")

	common_achievements = set(ACHIEVEMENTS)
	for name in players:
		common_achievements = common_achievements.intersection(players[name])
	print(f"Common achievements: {common_achievements}")

	for name in players:
		achievements_of_others: set[str] = set()
		for other_player in players:
			if other_player != name:
				achievements_of_others = achievements_of_others.union(players[other_player])
		only = players[name].difference(achievements_of_others)
		print(f"Only {name} has: {only}")

	for name in players:
		missing_achievements = set(ACHIEVEMENTS).difference(players[name])
		print(f"{name} is missing: {missing_achievements}")


if __name__ == "__main__":
	main()
