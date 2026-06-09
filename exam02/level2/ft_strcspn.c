/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcspn.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/09 16:47:22 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/09 17:15:11 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <stdio.h>
#include <stdlib.h>

size_t	ft_strcspn(const char *s, const char *reject)
{
	size_t i = 0;
	size_t j = 0;

	while(s[i])
	{
		j = 0;
		while(reject[j])
		{
			if(s[i] == reject[j])
				return(i);
			j++;
		}
		i++;
	}
	return(i);
}

int main(void)
{
	char s[] = "cippppppppoaz";
	char reject[] = "aoz";

	printf("%zu\n", ft_strcspn(s, reject));
	return(0);
}
