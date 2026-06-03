/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rrange.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 21:21:19 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/03 21:45:59 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>


int     *ft_rrange(int start, int end)
{
	int *arr;
	int i = 0;
	
	if(start > end)
		return(NULL);
	arr = malloc(sizeof(int) * (end - start + 1));
	if(!arr)
		return(NULL);
	while(end >= start)
	{
		arr[i] = end;
		end--;
		i++;
	}
	return(arr);
}

int main(void)
{
	int *arr;
	int start = -1;
	int end = 5;
	int size = end - start + 1;
	int i = 0;

	arr = ft_rrange(start, end);
	if(!arr)
		return(0);
		
	while(size > i)
	{
		printf("%d\n", arr[i]);
		i++;
	}
	free(arr);
}
