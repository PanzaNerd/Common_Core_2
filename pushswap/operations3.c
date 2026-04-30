/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations3.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/30 16:50:53 by mpanzani          #+#    #+#             */
/*   Updated: 2026/04/30 16:51:37 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	rr(t_node **a, t_node **b)
{
	rotate(a);
	rotate(b);
	print_op("rr");
}

static void	rev_rotate(t_node **s)
{
	t_node	*last;
	t_node	*penult;

	if (!*s || !(*s)->next)
		return ;
	last = *s;
	penult = NULL;
	while (last->next)
	{
		penult = last;
		last = last->next;
	}
	penult->next = NULL;
	last->next = *s;
	*s = last;
}

void	rra(t_node **a)
{
	rev_rotate(a);
	print_op("rra");
}

void	rrb(t_node **b)
{
	rev_rotate(b);
	print_op("rrb");
}

void	rrr(t_node **a, t_node **b)
{
	rev_rotate(a);
	rev_rotate(b);
	print_op("rrr");
}
