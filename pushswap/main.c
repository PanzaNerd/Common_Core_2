/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/07 23:20:10 by mpanzani          #+#    #+#             */
/*   Updated: 2026/04/07 23:54:43 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	main(int ac, char **av)
{
	t_node	*a;
	t_node	*b;

	if (ac < 2)
		return (0);
	a = NULL;
	b = NULL;
	parse_args(ac, av, &a);
	if (stack_size(a) == 1)
	{
		free_stack(&a);
		return (0);
	}
	assign_index(a);
	if (is_sorted(a))
	{
		free_stack(&a);
		return (0);
	}
	if (stack_size(a) == 2)
		sort_two(&a);
	else if (stack_size(a) == 3)
		sort_three(&a);
	else
		turk_sort(&a, &b);
	free_stack(&a);
	free_stack(&b);
	return (0);
}
