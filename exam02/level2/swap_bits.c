/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap_bits.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: matthias <matthias@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 16:42:30 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/25 16:27:07 by matthias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void print_bits(unsigned char octet)
{
	int i = 7;
	while (i >= 0)
	{
		if ((octet >> i) & 1)
			write(1, "1", 1);
		else
			write(1, "0", 1);
		i--;
	}
}

unsigned char swap_bits(unsigned char octet)
{
	return ((octet >> 4) | (octet << 4));
}

int	main(void)
{
	unsigned char result;

	result = swap_bits(5);
	print_bits(5);
	write(1, "\n", 1);
	print_bits(result);
	write(1, "\n", 1);
	
	return (0);
}
