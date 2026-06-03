/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_foreach.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 21:47:32 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/03 23:32:30 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list_foreach.h"

void stampa(void *data)
{
	printf("%s\n", (char *)data);
}

void	ft_list_foreach(t_list *begin_list, void (*f)(void *))
{
	t_list *list_ptr;

	list_ptr = begin_list;
	while (list_ptr)
	{
		(*f)(list_ptr->data);
		list_ptr = list_ptr->next;
	}
}

int main(void)
{
	t_list a;
	t_list b;
	t_list c;
	
	a.data = "primo";
	b.data = "secondo";
	c.data = "terzo";

	a.next = &b;
	b.next = &c;
	c.next = NULL;

	ft_list_foreach(&a, stampa);
    return (0);
}
