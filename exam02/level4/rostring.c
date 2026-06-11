/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rostring.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: matthias <matthias@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 23:53:13 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/11 15:46:15 by matthias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int main(int ac, char **av)
{
	int i = 0;
	int start = 0;
	int end = 0;
	int flag = 0;

	if (ac < 2)
	{
		write(1, "\n", 1);
		return (0);
	}
	// salta spazi iniziali
	while (av[1][i] == ' ' || av[1][i] == '\t')
		i++;
	start = i;
	// trova fine prima parola
	while (av[1][i] && av[1][i] != ' ' && av[1][i] != '\t')
		i++;
	end = i;
	// salta spazi dopo prima parola
	while (av[1][i] == ' ' || av[1][i] == '\t')
		i++;
	// stampa il resto (dopo la prima parola)
	while (av[1][i])
	{
		if (av[1][i] == ' ' || av[1][i] == '\t')
		{
			while (av[1][i] == ' ' || av[1][i] == '\t')
				i++;
			if (av[1][i])
				write(1, " ", 1);
		}
		else
		{
			write(1, &av[1][i], 1);
			i++;
			flag = 1;
		}
	}
	// spazio tra resto e prima parola (solo se c'è resto)
	if (flag)
		write(1, " ", 1);
	// stampa prima parola
	while (start < end)
	{
		write(1, &av[1][start], 1);
		start++;
	}
	write(1, "\n", 1);
	return (0);
}
