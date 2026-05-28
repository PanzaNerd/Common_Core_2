/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_bits.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 16:17:31 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/28 16:46:41 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	print_bits(unsigned char octet)
{
	int				i;
	unsigned char	mask;
	char			bit;

	i = 8;
	while (i > 0)
	{
		i--;
		mask = 1 << i;
		if (octet & mask)
			bit = '1';
		else
			bit = '0';
		write(1, &bit, 1);
	}
}

int	main(void)
{
	print_bits(2);
	write(1, "\n", 1);
	print_bits(5);
	write(1, "\n", 1);
	print_bits(255);
	write(1, "\n", 1);
	print_bits(0);
	write(1, "\n", 1);
	return (0);
}
