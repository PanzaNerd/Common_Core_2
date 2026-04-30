/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/07 23:32:44 by mpanzani          #+#    #+#             */
/*   Updated: 2026/04/30 17:11:27 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	swap(t_node **s)
{
	int	tmp_val;
	int	tmp_idx;

	if (!*s || !(*s)->next)
		return ;
	tmp_val = (*s)->value;
	tmp_idx = (*s)->index;
	(*s)->value = (*s)->next->value;
	(*s)->index = (*s)->next->index;
	(*s)->next->value = tmp_val;
	(*s)->next->index = tmp_idx;
}

void	sa(t_node **a)
{
	swap(a);
	print_op("sa");
}

void	sb(t_node **b)
{
	swap(b);
	print_op("sb");
}

void	ss(t_node **a, t_node **b)
{
	swap(a);
	swap(b);
	print_op("ss");
}

void	push(t_node **dst, t_node **src)
{
	t_node	*node;

	if (!*src)
		return ;
	node = *src;
	*src = (*src)->next;
	node->next = *dst;
	*dst = node;
}
