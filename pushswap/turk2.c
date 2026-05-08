/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   turk2.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/30 16:53:20 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/08 17:24:06 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_node	*find_min(t_node *a)
{
	t_node	*best;
	t_node	*ca;

	best = a;
	ca = a;
	while (ca)
	{
		if (ca->index < best->index)
			best = ca;
		ca = ca->next;
	}
	return (best);
}

t_node	*cheapest(t_node *b)
{
	t_node	*cb;
	t_node	*best;
	int		best_cost;

	cb = b;
	best = NULL;
	best_cost = INT_MAX;
	while (cb)
	{
		if (total_cost(cb) < best_cost)
		{
			best_cost = total_cost(cb);
			best = cb;
		}
		cb = cb->next;
	}
	return (best);
}

static void	do_rotations(t_node **a, t_node **b, int *ca, int *cb)
{
	while (*ca > 0 && *cb > 0)
	{
		rr(a, b);
		(*ca)--;
		(*cb)--;
	}
	while (*ca < 0 && *cb < 0)
	{
		rrr(a, b);
		(*ca)++;
		(*cb)++;
	}
}

static void	do_single_rotations(t_node **a, t_node **b, int ca, int cb)
{
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
}

void	do_move(t_node **a, t_node **b, t_node *node)
{
	int	ca;
	int	cb;

	ca = node->cost_a;
	cb = node->cost_b;
	do_rotations(a, b, &ca, &cb);
	do_single_rotations(a, b, ca, cb);
	pa(a, b);
}
