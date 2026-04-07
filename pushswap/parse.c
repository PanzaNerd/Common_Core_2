/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/07 23:20:31 by mpanzani          #+#    #+#             */
/*   Updated: 2026/04/07 23:43:45 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	ft_isdigit(char c)
{
	return (c >= '0' && c <= '9');
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
	while (*str)
	{
		result = result * 10 + (*str - '0');
		str++;
	}
	return (result * sign);
}

static int	is_valid(char *str)
{
	int	i;

	i = 0;
	if (str[i] == '-' || str[i] == '+')
		i++;
	if (!str[i])
		return (0);
	while (str[i])
	{
		if (!ft_isdigit(str[i]))
			return (0);
		i++;
	}
	return (1);
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
	t_node	*cur;
	t_node	*inner;
	int		idx;

	cur = a;
	while (cur)
	{
		idx = 0;
		inner = a;
		while (inner)
		{
			if (inner->value < cur->value)
				idx++;
			inner = inner->next;
		}
		cur->index = idx;
		cur = cur->next;
	}
}
