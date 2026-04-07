/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   turk.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/07 23:34:35 by mpanzani          #+#    #+#             */
/*   Updated: 2026/04/07 23:45:41 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	set_positions(t_node *a, t_node *b)
{
	int	i;

	i = 0;
	while (a)
	{
		a->pos = i++;
		a = a->next;
	}
	i = 0;
	while (b)
	{
		b->pos = i++;
		b = b->next;
	}
}

static void	set_target(t_node *a, t_node *b)
{
	t_node	*cb;
	t_node	*ca;
	t_node	*best;

	cb = b;
	while (cb)
	{
		best = NULL;
		ca = a;
		while (ca)
		{
			if (ca->index < cb->index)
				if (!best || ca->index > best->index)
					best = ca;
			ca = ca->next;
		}
		if (!best)
		{
			ca = a;
			while (ca)
			{
				if (!best || ca->index > best->index)
					best = ca;
				ca = ca->next;
			}
		}
		cb->target_pos = best->pos;
		cb = cb->next;
	}
}

static void	set_costs(t_node *b, int size_a, int size_b)
{
	t_node	*cur;

	cur = b;
	while (cur)
	{
		if (cur->pos <= size_b / 2)
			cur->cost_b = cur->pos;
		else
			cur->cost_b = -(size_b - cur->pos);
		if (cur->target_pos <= size_a / 2)
			cur->cost_a = cur->target_pos;
		else
			cur->cost_a = -(size_a - cur->target_pos);
		cur = cur->next;
	}
}

static int	abs_val(int n)
{
	return (n < 0 ? -n : n);
}

static int	total_cost(t_node *n)
{
	int	ca;
	int	cb;

	ca = n->cost_a;
	cb = n->cost_b;
	if (ca >= 0 && cb >= 0)
		return (ca > cb ? ca : cb);
	if (ca <= 0 && cb <= 0)
		return (abs_val(ca) > abs_val(cb) ? abs_val(ca) : abs_val(cb));
	return (abs_val(ca) + abs_val(cb));
}

static t_node	*cheapest(t_node *b)
{
	t_node	*cur;
	t_node	*best;
	int		best_cost;

	cur = b;
	best = NULL;
	best_cost = INT_MAX;
	while (cur)
	{
		if (total_cost(cur) < best_cost)
		{
			best_cost = total_cost(cur);
			best = cur;
		}
		cur = cur->next;
	}
	return (best);
}

static void	do_move(t_node **a, t_node **b, t_node *node)
{
	int	ca;
	int	cb;

	ca = node->cost_a;
	cb = node->cost_b;
	while (ca > 0 && cb > 0)
	{
		rr(a, b);
		ca--;
		cb--;
	}
	while (ca < 0 && cb < 0)
	{
		rrr(a, b);
		ca++;
		cb++;
	}
	while (cb > 0)
	{
		rb(b);
		cb--;
	}
	while (cb < 0)
	{
		rrb(b);
		cb++;
	}
	while (ca > 0)
	{
		ra(a);
		ca--;
	}
	while (ca < 0)
	{
		rra(a);
		ca++;
	}
	pa(a, b);
}

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

void	turk_sort(t_node **a, t_node **b)
{
	int		size;
	t_node	*node;

	size = stack_size(*a);
	while (size-- > 3)
		pb(a, b);
	sort_three(a);
	while (*b)
	{
		set_positions(*a, *b);
		set_target(*a, *b);
		set_costs(*b, stack_size(*a), stack_size(*b));
		node = cheapest(*b);
		do_move(a, b, node);
	}
	rotate_min(a);
}
