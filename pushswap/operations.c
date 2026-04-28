/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/07 23:32:44 by mpanzani          #+#    #+#             */
/*   Updated: 2026/04/28 20:58:16 by mpanzani         ###   ########.fr       */
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

static void	push(t_node **dst, t_node **src)
{
	t_node	*node;

	if (!*src)
		return ;
	node = *src;
	*src = (*src)->next;
	node->next = *dst;
	*dst = node;
}

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

static void	rotate(t_node **s)
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

void	rr(t_node **a, t_node **b)
{
	rotate(a);
	rotate(b);
	print_op("rr");
}

static void	rev_rotate(t_node **s)
{
	t_node	*cur;
	t_node	*prev;

	if (!*s || !(*s)->next)
		return ;
	cur = *s;
	prev = NULL;
	while (cur->next)
	{
		prev = cur;
		cur = cur->next;
	}
	prev->next = NULL;
	cur->next = *s;
	*s = cur;
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
