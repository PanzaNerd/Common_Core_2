/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 13:45:09 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/21 13:46:16 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

void ft_swap(int *a, int *b)
{
	int tmp;

	tmp = *a;
	*a = *b;
	*b = tmp;
}

int main(void)
{
    int a = 42;
    int b = 7;

    printf("PRIMA: a=%d b=%d\n", a, b);
    ft_swap(&a, &b);
    printf("DOPO:  a=%d b=%d\n", a, b);
    return (0);
}
