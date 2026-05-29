/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strpbrk.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/29 16:28:41 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/29 16:28:44 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	*arr;
	int	n;
	int	size;

	if (min >= max)
		return (NULL);
	size = max - min;
	arr = malloc(sizeof(int) * size);
	if (arr == NULL)
		return (NULL);
	n = 0;
	while (n < size)
	{
		arr[n] = min + n;
		n++;
	}
	return (arr);
}

/*int	main(void)
{
    int	min = 1;
    int	max = 100;
    int	size = max - min;
    int	*arr = ft_range(min, max);
    int n = 0;

    while (n < size)
    {
        printf("%d ", arr[n]);
        n++;
    }
    printf("\n");
    free(arr);
}*/
