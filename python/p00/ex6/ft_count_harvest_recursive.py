# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/26 23:05:34 by mpanzani          #+#    #+#              #
#    Updated: 2026/08/27 14:11:17 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	print_days(1, days)


def print_days(day, total):
	if day > total:
		print("Harvest time!")
	else:
		print(f"Day {day}")
		print_days(day + 1, total)

# ft_count_harvest_recursive()
