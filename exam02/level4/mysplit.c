/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   split.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 20:19:10 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/02 20:29:53 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

char    **ft_split(char *str)
{
	
}

int main (void)
{
	char **str;
	int i = 0;

	str = ft_split(" hello 	 world foo  ");
	
	while(str[i])
	{
		printf("%s\n", str[i]);
		i++;
	}
}
