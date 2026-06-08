/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   paramsum.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 18:42:53 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/08 19:17:59 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void ft_putnbr(int n)
{
	char c;

	if(n > 9)
		ft_putnbr(n/10);
	c = (n % 10) + '0';
	write(1, &c, 1);
}

int main(int ac, char **av)
{
	int n = 0;
	
	if(ac < 2)
	{
		write(1, "0\n", 2);
		return(0);
	}
	else
	{
		while(av[n])
			n++;
		ft_putnbr(n - 1);
	}
	write(1, "\n", 1);
	return(0);
}
