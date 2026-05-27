/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 17:29:10 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/27 18:35:22 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

char *ft_strdup(const char *s)
{
    int     i;
    char    *s2;

    if (!s)
        return (NULL);
    i = 0;
    while (s[i])
        i++;
    s2 = malloc(sizeof(char) * (i + 1));
    if (!s2)
        return (NULL);
    i = 0;
    while (s[i])
    {
        s2[i] = s[i];
        i++;
    }
    s2[i] = '\0';
    return (s2);
}

int main(void)
{
	char s[100] = "ciaooooo";

	printf("%s\n", ft_strdup(s));
}
