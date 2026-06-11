/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rev_wstr.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: matthias <matthias@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 18:24:42 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/11 15:37:36 by matthias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int ac, char **av)
{
	int i = 0;
	int end = 0;
	int start = 0;

	if(ac != 2)
	{
		write(1, "\n", 1);
		return(0);
	}
	while(av[1][i])
		i++;
	while(i > 0)
	{
		while(i > 0 && (av[1][i - 1] == ' ' || av[1][i - 1] == '\t'))
			i--;
		end = i;
		while(i > 0 && av[1][i - 1] != ' ' && av[1][i - 1] != '\t')
			i--;
		start = i;
		while(start < end)
		{
			write(1, &av[1][start], 1);
			start++;
		}
		if(i > 0)
			write(1, " ", 1);
	}
	write(1, "\n", 1);
	return(0);
}
