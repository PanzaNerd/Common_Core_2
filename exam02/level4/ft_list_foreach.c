/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_foreach.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 21:47:32 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/03 22:13:48 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list_foreach.h"

char ft_toupper(char *a)
{
	while(*a)
	{
		*a = *a - 32;
		*a++;
	}
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

	printf("%s\n", ft_list_foreach(&a, ft_toupper));
    printf("%s: %d\n", ft_list_foreach(&b, ft_toupper));
    printf("%s\n", ft_list_foreach(NULL, ft_toupper));
    return (0);
}
