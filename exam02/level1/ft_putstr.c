/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/20 19:32:28 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/21 13:07:36 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putstr(char *str)
{
	int i = 0;
	
	while(str[i])
	{
		write(1, &str[i], 1);
		i++;
	}
}

int	main(void)
{
	char str[]= "krankenwagen";
	
	ft_putstr(str);
	write(1, "\n", 1);
	return(0);
}
