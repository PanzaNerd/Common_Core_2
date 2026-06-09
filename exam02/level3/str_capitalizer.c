/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   str_capitalizer.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 22:12:18 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/09 15:45:17 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int main(int ac, char **av)
{
	int n = 1;
	int i;

	if (ac == 1)
	{
		write(1, "\n", 1);
		return (0);
	}
	while (n < ac)
	{
		i = 0;
		while (av[n][i])
		{
			if (av[n][i] >= 'a' && av[n][i] <= 'z')
				av[n][i] = av[n][i] + 32;

			if (i > 0 && (av[n][i - 1] >= 'a' && av[n][i - 1] <= 'z'
				|| av[n][i - 1] >= 'A' && av[n][i - 1] <= 'Z'))
			{
				if (av[n][i] >= 'A' && av[n][i] <= 'Z')
					av[n][i] = av[n][i] + 32;
			}

			write(1, &av[n][i], 1);
			i++;
		}
		write(1, "\n", 1);
		n++;
	}
	return (0);
}
