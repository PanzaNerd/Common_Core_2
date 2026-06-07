/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tab_mult.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/07 19:34:54 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/07 22:13:00 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void ft_putnbr(int i)
{
	int result;
	
	if(i > 9)
		ft_putnbr(i / 10);
	result = (i % 10) + '0';
	write(1, &result, 1);
}

int ft_atoi(char *str)
{
	int result = 0;
	int i = 0;
	
	while(str[i] == ' ' || (str[i] >= 9 && str[i] <= 13))
		i++;
	while(str[i] >= '0' && str[i] <= '9')
	{
		result = result * 10 + (str[i] - '0');
		i++;
	}
	return(result);
}

int main(int ac, char **av)
{
	int n;
	int i;
	
	if(ac != 2)
	{
		write(1, "\n", 1);
		return(0);
	}
	n = ft_atoi(av[1]);
	i = 1;
	
	while(i <= 9)
	{
		ft_putnbr(i);
		write(1, " x ", 3);
		ft_putnbr(n);
		write(1, " = ", 3);
		ft_putnbr(i * n);
		write(1, "\n", 1);
		i++;
	}
	return(0);
}
