/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/07 23:20:10 by mpanzani          #+#    #+#             */
/*   Updated: 2026/04/17 21:31:56 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	main(int ac, char **av)
{
	t_node	*a;
	t_node	*b;
	int		size;

	if (ac < 2)
		return (0);
	a = NULL;
	b = NULL;
	parse_args(ac, av, &a);
	size = stack_size(a);
	if (size <= 1 || is_sorted(a))
		return (free_stack(&a), 0);
	assign_index(a);
	if (size == 2)
		sort_two(&a);
	else if (size == 3)
		sort_three(&a);
	else
		turk_sort(&a, &b);
	free_stack(&a);
	free_stack(&b);
	return (0);
}
