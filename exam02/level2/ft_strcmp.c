/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 21:27:00 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/27 21:44:57 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int    ft_strcmp(char *s1, char *s2)
{
    int i = 0;
	
    while (s1[i] && s1[i] == s2[i])
    {
        i++;
    }
    return (s1[i] - s2[i]);
}

int main(void)
{
	char s1[] = "acd";
	char s2[] = "abc";
	
	printf("%d\n", ft_strcmp(s1, s2));
	return(0);
}
