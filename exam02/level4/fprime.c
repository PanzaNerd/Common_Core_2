/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fprime.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 23:48:29 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/03 23:48:31 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
	int i;
	int number;

	if (ac != 2)
	{
		printf("\n");
		return (0);
	}
	number = atoi(av[1]);
	if (number == 1)
	{
		printf("1\n");
		return (0);
	}
	i = 2;
	while (i <= number)
	{
		if (number % i == 0)
		{
			printf("%d", i);
			number = number / i;
			if (number != 1)
				printf("*");
			i = 2;
		}
		else
			i++;
	}
	printf("\n");
	return (0);
}
