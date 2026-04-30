/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations2.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/30 16:49:35 by mpanzani          #+#    #+#             */
/*   Updated: 2026/04/30 17:15:10 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	pa(t_node **a, t_node **b)
{
	push(a, b);
	print_op("pa");
}

void	pb(t_node **a, t_node **b)
{
	push(b, a);
	print_op("pb");
}

void	rotate(t_node **s)
{
	t_node	*first;
	t_node	*last;

	if (!*s || !(*s)->next)
		return ;
	first = *s;
	last = *s;
	while (last->next)
		last = last->next;
	*s = first->next;
	first->next = NULL;
	last->next = first;
}

void	ra(t_node **a)
{
	rotate(a);
	print_op("ra");
}

void	rb(t_node **b)
{
	rotate(b);
	print_op("rb");
}
