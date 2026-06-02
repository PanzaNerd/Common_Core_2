/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rev_wstr.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 18:24:42 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/02 19:32:48 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int main(int ac, char **av)
{
    int i;
    int end;
    int first;

    if (ac != 2)
    {
        write(1, "\n", 1);
        return (0);
    }
    i = 0;
    while (av[1][i])
        i++;
    first = 1;
    while (i > 0)
    {
        while (i > 0 && (av[1][i - 1] == ' ' || av[1][i - 1] == '\t'))
            i--;
        end = i;
        while (i > 0 && av[1][i - 1] != ' ' && av[1][i - 1] != '\t')
            i--;
        if (end > i)
        {
            if (first == 0)
                write(1, " ", 1);
            write(1, &av[1][i], end - i);
            first = 0;
        }
    }
    write(1, "\n", 1);
    return (0);
}
