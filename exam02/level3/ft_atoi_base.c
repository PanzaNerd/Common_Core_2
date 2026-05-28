/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 13:58:52 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/28 14:58:42 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_atoi_base(const char *str, int str_base)
{
	int result = 0;
	int sign = 1;
	int i = 0;
	int val;
	
	while(str[i] == ' ' || (str[i] >= 9 && str[i] <= 13))
		i++;
	if(str[i] == '-')
		sign = -1;
	if(str[i] == '-' || str[i] == '+')
		i++;
	while(str[i])
	{
		if(str[i] >= '0' && str[i] <= '9')
			val = str[i] - '0';
		else if (str[i] >= 'a' && str[i] <= 'f')
			val = str[i] - 'a' + 10;
		else if (str[i] >= 'A' && str[i] <= 'F')
			val = str[i] - 'A' + 10;
		else
			break ;
		if (val >= str_base)
			break ;
		result = result * str_base + val;
		i++;
	}
	return(result * sign);
}

int main(void)
{
	printf("%d\n", ft_atoi_base("ff", 16));
	printf("%d\n", ft_atoi_base("10", 2));
	printf("%d\n", ft_atoi_base("10", 8));
	printf("%d\n", ft_atoi_base("-ff", 16));
	return (0);
}
