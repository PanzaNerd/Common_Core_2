/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   do_op.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/09 15:47:45 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/09 16:18:51 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main(int ac, char **av)
{
	int result;

	if (ac != 4)
	{
		write(1, "\n", 1);
		return (0);
	}

	if (av[2][0] == '+')
		result = atoi(av[1]) + atoi(av[3]);
	else if (av[2][0] == '-')
		result = atoi(av[1]) - atoi(av[3]);
	else if (av[2][0] == '*')
		result = atoi(av[1]) * atoi(av[3]);
	else if (av[2][0] == '/')
		result = atoi(av[1]) / atoi(av[3]);
	else if (av[2][0] == '%')
		result = atoi(av[1]) % atoi(av[3]);
	else
	{
		write(1, "\n", 1);
		return (0);
	}

	printf("%d\n", result);
	return (0);
}
