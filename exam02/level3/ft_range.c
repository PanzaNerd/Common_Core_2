/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/29 17:01:29 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/29 17:33:04 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

int	*ft_range(int min, int max)
{
	int	*arr;
	int	size;
	int	i;

	if (min > max)
		return (NULL);

	size = max - min + 1;

	arr = malloc(sizeof(int) * size);
	if (!arr)
		return (NULL);

	i = 0;
	while (min <= max)
	{
		arr[i] = min;
		i++;
		min++;
	}
	return (arr);
}

int	main(void)
{
	int	*arr;
	int	i;
	int	size;

	arr = ft_range(-1, 5);

	if (arr == NULL)
		return (0);

	size = 5 - (-1) + 1;

	i = 0;
	while (i < size)
	{
		printf("%d\n", arr[i]);
		i++;
	}

	free(arr);
	return (0);
}
