/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 13:07:50 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/21 13:33:19 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

char	*ft_strcpy(char *s1, char *s2)
{
	int	i = 0;

	while(s2[i])
	{
		s1[i] = s2[i];
		i++;
	}
	s1[i] = '\0';
	return(s1);
}

int main(void)
{
	char src[]= "CIAO ANIMALE";
	char dst[50]= "pangrattato";

	printf("PRIMA\nsrc:%s\ndst:%s\n", src, dst);
	ft_strcpy(dst, src);
	printf("DOPO\nsrc:%s\ndst:%s\n", src, dst);
}
