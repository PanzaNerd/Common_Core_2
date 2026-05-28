/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   str_capitalizer.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 22:12:18 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/28 13:53:39 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int main(int ac, char **av)
{
	int i = 0;
	int n = 1;
	int new_word = 1;

	if(ac == 1)
	{
		write(1, "\n", 1);
		return(0);
	}
	while(n < ac)
	{
		i = 0;
		new_word = 1;
		while(av[n][i])
		{
			if(av[n][i] == ' ' || av[n][i] == '\t')
				new_word = 1;
			else if(new_word == 1)
			{
				if (av[n][i] >= 'a' && av[n][i] <= 'z')
                    av[n][i] = av[n][i] - 32;
                new_word = 0;
			}
			else if (av[n][i] >= 'A' && av[n][i] <= 'Z')
                av[n][i] = av[n][i] + 32;
            write(1, &av[n][i], 1);
            i++;
		}
		write(1, "\n", 1);
        n++;
	}
	return(0);
}
