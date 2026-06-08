/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rstr_capitalizer.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 20:05:27 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/08 20:42:30 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	main(int ac, char **av)
{
	int		i;
	int		n;
	char	c;

	n = 1;
	if (ac == 1)
		write(1, "\n", 1);
	while (n < ac)
	{
		i = 0;
		while (av[n][i])
		{
			c = av[n][i];

			if (c >= 'A' && c <= 'Z')
				c = c + 32;

			if ((c >= 'a' && c <= 'z') && (!(av[n][i + 1] >= 'a' && av[n][i + 1] <= 'z') && !(av[n][i + 1] >= 'A' && av[n][i + 1] <= 'Z')))
				c = c - 32;

			write(1, &c, 1);
			i++;
		}
		write(1, "\n", 1);
		n++;
	}
	return (0);
}
