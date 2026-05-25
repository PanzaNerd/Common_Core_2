/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   wdmatch.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 21:59:21 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/25 23:35:34 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int main(int ac, char **av)
{
	int i = 0;
	int j = 0;
	int x = 0;

	if(ac != 3)
	{
		write(1, "\n", 1);
		return(0);
	}
	while(av[1][x])
		x++;
	while(av[2][j])
	{
		if(av[1][i] == av[2][j])
			i++;
		j++;
	}
	if(i != x)
	{
		write(1, "\n", 1);
		return(0);
	}
	i = 0;
	j = 0;
	while(av[2][j])
	{
		if(av[1][i] == av[2][j])
		{
			write(1, &av[1][i], 1);
			i++;
		}	
		j++;
	}
	write(1, "\n", 1);
}
