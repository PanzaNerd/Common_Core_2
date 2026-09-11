# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_alchemist.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/11 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/11 10:00:00 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random


def main() -> None:
	print("=== Game Data Alchemist ===")

	players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
	print(f"Initial list of players: {players}")

	capitalized = [name.capitalize() for name in players]
	print(f"New list with all names capitalized: {capitalized}")

	already_capitalized = [name for name in players if name[0].isupper()]
	print(f"New list of capitalized names only: {already_capitalized}")

	scores = {name: random.randint(50, 1000) for name in capitalized}
	print(f"Score dict: {scores}")

	average = sum(scores.values()) / len(scores)
	print(f"Score average is {round(average, 2)}")

	high_scores = {name: score for name, score in scores.items() if score > average}
	print(f"High scores: {high_scores}")


if __name__ == "__main__":
	main()
