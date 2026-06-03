/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rostring.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 23:53:13 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/04 00:37:53 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
	int i = 0;
	int start;
	int end;
	int flag;
	int printed;

	if(ac > 1)
	{
		while(av[1][i] == ' ' || av[1][i] == '\t')
			i++;
		start = i;
		while(av[1][i] && av[1][i] != ' ' && av[1][i] != '\t')
			i++;
		end = i;
		while(av[1][i] == ' ' || av[1][i] == '\t')
			i++;
		flag = 0;
		printed = 0;
		while(av[1][i])
		{
			if(av[1][i] == ' ' || av[1][i] == '\t')
				flag = 1;
			else
			{
				if(flag)
					write(1, " ", 1);
				flag = 0;
				write(1, &av[1][i], 1);
				printed = 1;
			}
			i++;
		}
		if(start < end && printed)
			write(1, " ", 1);
		while(start < end)
		{
			write(1, &av[1][start], 1);
			start++;
		}
	}
	write(1, "\n", 1);
	return(0);
}
