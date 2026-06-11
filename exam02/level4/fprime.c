/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fprime.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: matthias <matthias@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 23:48:29 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/11 14:52:30 by matthias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

int main(int ac, char **av)
{
	unsigned int number;
	unsigned int i = 2;

	if(ac != 2)
	{
		printf("\n");
		return(0);
	}

	number = atoi(av[1]);

	if (number == 1)
	{
		printf("1\n");
		return(0);
	}

	while(i <= number)
	{
		if(number % i == 0)
		{
			printf("%d", i);
			number = number / i;
			if(number != 1)
				printf("*");
			i = 2;
		}
		else
			i++;
	}
	printf("\n");
	return(0);
}
