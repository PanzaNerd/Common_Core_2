/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverse_bits.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 16:45:45 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/21 16:47:02 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	print_bits(unsigned char octet);

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

unsigned char reverse_bits(unsigned char octet)
{
	unsigned char	result;
	int				i;

	result = 0;
	i = 0;
	while (i < 8)
	{
		result = result << 1;
		result = result | (octet & 1);
		octet = octet >> 1;
		i++;
	}
	return (result);
}

int	main(void)
{
	print_bits(5);
	write(1, "\n", 1);
	print_bits(reverse_bits(5));
	write(1, "\n", 1);
	return (0);
}
