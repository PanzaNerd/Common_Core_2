/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: matthias <matthias@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 15:27:07 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/11 17:05:14 by matthias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

int count_digits(long num)
{
	int len = 0;

	//se il numero è negativo, rendiamolo positivo.(len include anche il segno)
	if (num <= 0)
	{
		len = 1;
		num = - num;
	}

	while (num > 0)
	{
		num = num / 10;
		len++;
	}
	return (len);
}

char *ft_itoa(int nbr)
{
	long  num = nbr;
	int   len;
	char *arr;

	// 1. conta + alloca + termina
	len = count_digits(num);
	arr = malloc(len + 1);
	if (!arr)
		return (NULL);
	arr[len] = '\0';

	// 2. gestisci segno e zero
	num = nbr;
	if (num < 0)
	{
		arr[0] = '-';
		num = - num;
	}
	
	if (num == 0)
		arr[0] = '0';

	// 3. riempi all'indietro
	while (num > 0)
	{
		len--;
		arr[len] = (num % 10) + '0';
		num = num / 10;
	}
	return (arr);
}

int main(void)
{
	int number = -12345;
	char *str = ft_itoa(number);
	if (str)
	{
		printf("La stringa che rappresenta %d e': %s\n", number, str);
		free(str);
	}
	return(0);
}

