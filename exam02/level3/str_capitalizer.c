/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   str_capitalizer.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 22:12:18 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/27 22:29:23 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int main(int ac, char **av)
{
	int i = 0;
	int n = 0;

	if(ac == 1)
	{
		write(1, "\n", 1);
		return(0);
	}
	
	while(av[n][i] && n > 0)
	{
		i = 0;
		if(i = 0)
		{
			av[n][i] = av[n][i] + 32;
			write(1, &av[n][i], 1);
		}
		i++;
		while(av[n][i] != ' ' || av[n][i] != '\t')
			write(1, &av[n][i], 1);
		while (av[n][i] == ' ' || av[n][i] == '\t')
		{
			i++;
			n++;
		}
	}
}
