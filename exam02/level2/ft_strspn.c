/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strspn.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 19:47:33 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/09 17:31:42 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

size_t ft_strspn(const char *s, const char *accept)
{
	size_t i = 0;
	size_t j = 0;

	while (s[i])
	{
		j = 0;
		while (accept[j])
		{
			if (s[i] == accept[j])
				break;
			j++;
		}
		if (accept[j] == '\0')
			return (i);
		i++;
	}
	return (i);
}

int main(void)
{
	char s[] = "ammutoliscimmia";
	char accept[] = "amm|to";

	printf("%zu\n", ft_strspn(s, accept));
	return(0);
}
