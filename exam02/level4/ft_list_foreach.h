/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_foreach.h                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 21:49:45 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/03 23:32:43 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_LIST_FOREACH_H
# define FT_LIST_FOREACH_H

#include <stdio.h>
#include <stdlib.h>

typedef struct    s_list
{
    struct s_list *next;
    void          *data;
}                 t_list;

void    ft_list_foreach(t_list *begin_list, void (*f)(void *));
void	stampa(void *data);

#endif
