# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/10 10:00:00 by mpanzani          #+#    #+#              #
#    Updated: 2026/09/10 10:00:00 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main() -> None:
	print("=== Command Quest ===")
	print(f"Program name: {sys.argv[0]}")

	if len(sys.argv) == 1:
		print("No arguments provided!")
	else:
		print(f"Arguments received: {len(sys.argv) - 1}")
		for i in range(1, len(sys.argv)):
			print(f"Argument {i}: {sys.argv[i]}")

	print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
	main()
