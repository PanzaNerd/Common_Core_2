/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ulstr.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/20 17:37:07 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/20 17:49:53 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int main(int ac, char **av)
{
	int i = 0;
	char c;
	
	if(ac != 2)
	{
		write(1, "\n", 1);
		return(0);
	}
	while(av[1][i])
	{
		if(av[1][i] >= 'a' && av[1][i] <= 'z')
		{
			c = av[1][i] - 32;
			write(1, &c, 1);
		}
		else if(av[1][i] >= 'A' && av[1][i] <= 'Z')
		{
			c = av[1][i] + 32;
			write(1, &c, 1);
		}
		else
			write(1, &av[1][i], 1);
		i++;
	}
	write(1, "\n", 1);
	return(0);
}


