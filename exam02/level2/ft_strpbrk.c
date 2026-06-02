/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strpbrk.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/29 16:28:41 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/02 22:19:50 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
//strpbrk trova il primo carattere di s1 che appare in s2 e restituisce un puntatore a quel carattere. Se non trova niente restituisce NULL
char	*ft_strpbrk(const char *s1, const char *s2)
{
	int i;
	int j;

	i = 0;
	while (s1[i])
	{
		j = 0;
		while (s2[j])
		{
			if (s1[i] == s2[j])
				return ((char *)&s1[i]);
			j++;
		}
		i++;
	}
	return (NULL);
}

int main(void)
{
	char s1[] = "mammut";
	char s2[] = "xu";

	printf("%s\n", ft_strpbrk(s1, s2));
	return(0);
}
