# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/26 22:48:41 by mpanzani          #+#    #+#              #
#    Updated: 2026/08/27 14:09:03 by mpanzani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	for i in range(1, days + 1):
		print(f"Day {i}")
	print("Harvest time!")

# ft_count_harvest_iterative()
