/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/07 23:20:43 by mpanzani          #+#    #+#             */
/*   Updated: 2026/04/30 17:28:11 by mpanzani         ###   ########.fr       */
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
void	print_op(char *str);

void	error_exit(t_node **a, t_node **b);
int		is_sorted(t_node *stack);

void	parse_args(int ac, char **av, t_node **a);
void	assign_index(t_node *a);

void	push(t_node **dst, t_node **src);
void	sa(t_node **a);
void	sb(t_node **b);
void	ss(t_node **a, t_node **b);

void	rotate(t_node **s);
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

void	set_positions(t_node *a, t_node *b);
void	set_target(t_node *b, t_node *a);
void	set_costs(t_node *b, int size_a, int size_b);
int		total_cost(t_node *n);

t_node	*find_min(t_node *a);
t_node	*cheapest(t_node *b);
void	do_move(t_node **a, t_node **b, t_node *node);

void	turk_sort(t_node **a, t_node **b);

#endif
