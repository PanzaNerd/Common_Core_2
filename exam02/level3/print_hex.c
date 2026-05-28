/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_hex.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 17:39:40 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/28 17:39:43 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	print_hex(unsigned int n)
{
	char	*hex;

	hex = "0123456789abcdef";
	if (n >= 16)
		print_hex(n / 16);
	write(1, &hex[n % 16], 1);
}

int	main(void)
{
	print_hex(255);
	write(1, "\n", 1);
	print_hex(16);
	write(1, "\n", 1);
	print_hex(0);
	write(1, "\n", 1);
	return (0);
}
