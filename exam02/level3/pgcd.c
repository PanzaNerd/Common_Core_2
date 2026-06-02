/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pgcd.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 19:39:44 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/02 19:58:55 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int pgcd(int a, int b)
{
    while (b != 0)
    {
        int tmp = b;
        b = a % b;
        a = tmp;
    }
    return (a);
}

int main(int ac, char **av)
{
    if (ac != 3)
    {
        printf("\n");
        return (0);
    }
    printf("%d\n", pgcd(atoi(av[1]), atoi(av[2])));
    return (0);
}
