/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_size.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 16:10:50 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/29 16:58:59 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_list_size.h"

int	ft_list_size(t_list *begin_list)
{
	int	count;

	count = 0;
	while (begin_list)
	{
		count++;
		begin_list = begin_list->next;
	}
	return (count);
}

int	main(void)
{
    t_list	a;
    t_list	b;
    t_list	c;

    a.data = "primo";
    b.data = "secondo";
    c.data = "terzo";

    a.next = &b;
    b.next = &c;
    c.next = NULL;

    printf("size: %d\n", ft_list_size(&a));
    printf("size: %d\n", ft_list_size(&b));
    printf("size: %d\n", ft_list_size(NULL));
    return (0);
}
