/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   union.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 20:44:39 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/27 21:24:20 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int main(int ac, char **av)
{
	int i = 0;
	int j = 0;
	int x = 0;
	char printed[256];
	
	if(ac != 3)
	{
		write(1, "\n", 1);
		return(0);
	}
	while(x < 256)
	{
		printed[x] = 0;
		x++;
	}
	while (av[1][i])
    {
        if (printed[av[1][i]] == 0)
        {
            printed[av[1][i]] = 1;
            write(1, &av[1][i], 1);
        }
        i++;
    }
    while (av[2][j])
    {
        if (printed[av[2][j]] == 0)
        {
            printed[av[2][j]] = 1;
            write(1, &av[2][j], 1);
        }
        j++;
    }
    write(1, "\n", 1);
    return (0);
}
