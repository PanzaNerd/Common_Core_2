/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   inter.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 18:36:53 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/27 20:26:24 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int main(int ac, char **av)
{
    int     i;
    int     j;
    int     x;
    char    printed[256];

    if (ac != 3)
    {
        write(1, "\n", 1);
        return (0);
    }
    x = 0;
    while (x < 256)
	{
        printed[x] = 0;
		x++;
	}
    i = 0;
    while (av[1][i])
    {
        j = 0;
        while (av[2][j] && av[2][j] != av[1][i])
            j++;
        if (av[2][j] == av[1][i] && printed[av[1][i]] == 0)
        {
            printed[av[1][i]] = 1;
            write(1, &av[1][i], 1);
        }
        i++;
    }
    write(1, "\n", 1);
    return (0);
}
