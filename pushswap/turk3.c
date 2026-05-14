/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   turk3.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/30 16:54:16 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/11 17:54:18 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	rotate_min(t_node **a)
{
	int		size;
	int		pos;
	t_node	*cur;

	size = stack_size(*a);
	pos = 0;
	cur = *a;
	while (cur->index != 0)
	{
		pos++;
		cur = cur->next;
	}
	if (pos <= size / 2)
		while (pos-- > 0)
			ra(a);
	else
	{
		pos = size - pos;
		while (pos-- > 0)
			rra(a);
	}
}

static void	push_to_b(t_node **a, t_node **b)
{
	int	size;
	int	groups;
	int	group_size;
	int	pushed;

	size = stack_size(*a);
	if (size <= 100)
		groups = 5;
	else
		groups = 11;
	group_size = size / groups;
	pushed = 0;
	while (stack_size(*a) > 3)
	{
		if ((*a)->index <= pushed + group_size)
		{
			pb(a, b);
			if ((*b)->index < pushed - group_size / 2)
				rb(b);
			pushed++;
		}
		else
			ra(a);
	}
}

void	turk_sort(t_node **a, t_node **b)
{
	t_node	*node;

	push_to_b(a, b);
	sort_three(a);
	while (*b)
	{
		set_positions(*a, *b);
		set_target(*b, *a);
		set_costs(*b, stack_size(*a), stack_size(*b));
		node = cheapest(*b);
		do_move(a, b, node);
	}
	rotate_min(a);
}
