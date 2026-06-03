/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strspn.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 19:47:33 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/03 20:13:46 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

size_t ft_strspn(const char *s, const char *accept)
{
	size_t i = 0;
	size_t j = 0;

	while(s[i])
	{
		if(s[i] == accept[j])
		{
			i++;
		}
		j++;
	}
	return(i);
}

int main(void)
{
	char s[] = "ammutolisciti";
	char accept[] = "sci";

	printf("%lu\n", ft_strspn(s, accept));
}
