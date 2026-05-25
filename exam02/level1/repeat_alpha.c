/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   repeat_alpha.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 13:47:35 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/21 13:47:38 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int main(int ac, char **av)
{
    int i = 0;
    int j;
    int rep;

    if (ac != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    while (av[1][i])
    {
        if (av[1][i] >= 'a' && av[1][i] <= 'z')
            rep = av[1][i] - 'a' + 1;
        else if (av[1][i] >= 'A' && av[1][i] <= 'Z')
            rep = av[1][i] - 'A' + 1;
        else
            rep = 1;
        j = 0;
        while (j < rep)
        {
            write(1, &av[1][i], 1);
            j++;
        }
        i++;
    }
    write(1, "\n", 1);
    return (0);
}
