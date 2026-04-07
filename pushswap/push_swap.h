/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/07 23:20:43 by mpanzani          #+#    #+#             */
/*   Updated: 2026/04/07 23:26:03 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdlib.h>
# include <limits.h>
# include <unistd.h>

typedef struct s_node
{
	int				value;
	int				index;
	int				pos;
	int				target_pos;
	int				cost_a;
	int				cost_b;
	struct s_node	*next;
}	t_node;

t_node	*new_node(int value);
void	push_node(t_node **stack, int value);
int		stack_size(t_node *stack);
void	free_stack(t_node **stack);
int		is_sorted(t_node *stack);
void	error_exit(t_node **a, t_node **b);
void	print_op(char *str);

void	parse_args(int ac, char **av, t_node **a);
void	assign_index(t_node *a);

void	sa(t_node **a);
void	sb(t_node **b);
void	ss(t_node **a, t_node **b);
void	pa(t_node **a, t_node **b);
void	pb(t_node **a, t_node **b);
void	ra(t_node **a);
void	rb(t_node **b);
void	rr(t_node **a, t_node **b);
void	rra(t_node **a);
void	rrb(t_node **b);
void	rrr(t_node **a, t_node **b);

void	sort_two(t_node **a);
void	sort_three(t_node **a);
void	turk_sort(t_node **a, t_node **b);

#endif
