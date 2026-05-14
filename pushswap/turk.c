/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   turk.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/07 23:34:35 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/12 23:45:09 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	set_positions(t_node *a, t_node *b)
{
	int	i;

	i = 0;
	while (a)
	{
		a->pos = i;
		i++;
		a = a->next;
	}
	i = 0;
	while (b)
	{
		b->pos = i;
		i++;
		b = b->next;
	}
}

void	set_target(t_node *b, t_node *a)

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
			if (ca->index > cb->index)
				if (!best || ca->index < best->index)
					best = ca;
			ca = ca->next;
		}
		if (!best)
			best = find_min(a);
		cb->target_pos = best->pos;
		cb = cb->next;
	}
}

void	set_costs(t_node *b, int size_a, int size_b)
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
	if (n < 0)
		return (-n);
	return (n);
}

int	total_cost(t_node *n)
{
	int	csa;
	int	csb;

	csa = n->cost_a;
	csb = n->cost_b;
	if (csa >= 0 && csb >= 0)
	{
		if (csa > csb)
			return (csa);
		return (csb);
	}
	if (csa <= 0 && csb <= 0)
	{
		if (abs_val(csa) > abs_val(csb))
			return (abs_val(csa));
		return (abs_val(csb));
	}
	return (abs_val(csa) + abs_val(csb));
}
