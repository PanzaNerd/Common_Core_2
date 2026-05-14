/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/07 23:20:31 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/12 17:54:46 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	is_valid(char *str)
{
	int	i;

	i = 0;
	if (!str || !str[0])
		return (0);
	if (str[i] == '-' || str[i] == '+')
		i++;
	if (!str[i])
		return (0);
	while (str[i])
	{
		if (str[i] < '0' || str[i] > '9')
			return (0);
		i++;
	}
	return (1);
}

static long	ft_atol(const char *str)
{
	long	result;
	int		sign;

	result = 0;
	sign = 1;
	if (*str == '-' || *str == '+')
	{
		if (*str == '-')
			sign = -1;
		str++;
	}
	while (*str >= '0' && *str <= '9')
	{
		result = result * 10 + (*str - '0');
		if (result * sign > INT_MAX)
			return ((long)INT_MAX + 1);
		if (result * sign < INT_MIN)
			return ((long)INT_MIN - 1);
		str++;
	}
	return (result * sign);
}

static int	has_dup(t_node *stack, int val)
{
	while (stack)
	{
		if (stack->value == val)
			return (1);
		stack = stack->next;
	}
	return (0);
}

void	parse_args(int ac, char **av, t_node **a)
{
	int		i;
	long	val;

	i = ac - 1;
	while (i >= 1)
	{
		if (!is_valid(av[i]))
			error_exit(a, NULL);
		val = ft_atol(av[i]);
		if (val > INT_MAX || val < INT_MIN)
			error_exit(a, NULL);
		if (has_dup(*a, (int)val))
			error_exit(a, NULL);
		push_node(a, (int)val);
		i--;
	}
}

void	assign_index(t_node *a)
{
	t_node	*ca;
	t_node	*ca2;
	int		idx;

	ca = a;
	while (ca)
	{
		idx = 0;
		ca2 = a;
		while (ca2)
		{
			if (ca2->value < ca->value)
				idx++;
			ca2 = ca2->next;
		}
		ca->index = idx;
		ca = ca->next;
	}
}
