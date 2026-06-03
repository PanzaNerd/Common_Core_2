/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrev.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 17:51:14 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/03 19:27:51 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

char    *ft_strrev(char *str)
{
	int i = 0;
	int len = 0;
	char temp;
	
	while(str[len])
		len++;
	while(i < len/2)
	{
		temp = str[i];
		str[i] = str[len - 1];
		str[len - 1] = temp;
		i++;
		len--;
	}
	return(str);
}

int main(void)
{
	char str[] = "abcde";
	
	printf("%s\n", ft_strrev(str));
}
