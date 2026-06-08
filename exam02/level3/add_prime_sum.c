/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   add_prime_sum.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 17:18:15 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/08 18:40:12 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putnbr(int n)
{
	char c;

	if (n >= 10)
		ft_putnbr(n / 10);
	c = (n % 10) + '0';
	write(1, &c, 1);
}

int	ft_atoi(char *str)
{
	int result;

	result = 0;
	while (*str >= '0' && *str <= '9')
	{
		result = result * 10 + (*str - '0');
		str++;
	}
	return (result);
}

int	is_prime(int n)
{
	int i;

	if (n < 2)
		return (0);
	i = 2;
	while (i * i <= n)
	{
		if (n % i == 0)
			return (0);
		i++;
	}
	return (1);
}

int	main(int ac, char **av)
{
	int	n;
	int	i;
	int	sum;

	if (ac != 2)
	{
		write(1, "0\n", 2);
		return (0);
	}
	n = ft_atoi(av[1]);
	if (n <= 0)
	{
		write(1, "0\n", 2);
		return (0);
	}
	i = 2;
	sum = 0;
	while (i <= n)
	{
		if (is_prime(i))
			sum = sum + i;
		i++;
	}
	ft_putnbr(sum);
	write(1, "\n", 1);
	return (0);
}
