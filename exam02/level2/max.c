/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   max.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/09 16:21:29 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/09 16:45:03 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int max(int* tab, unsigned int len)
{
	unsigned int i;
	int largest;

	if (len == 0)
		return (0);

	largest = tab[0];
	i = 1;

	while (i < len)
	{
		if (tab[i] > largest)
			largest = tab[i];
		i++;
	}
	return (largest);
}
int main(void)
{
	int tab = {-1, 0, 1, 2, 3, 4, 5};
	int len = 7;
	printf("%d", max(tab, len));
	return(0);
}
