/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 13:33:28 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/21 13:41:42 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

int	ft_strlen(char *str)
{
    int i = 0;

    while (str[i])
        i++;
    return (i);
}

int main(void)
{
	char str[] = "abcd";
	int len = ft_strlen(str);
	
	printf("%s\n%d\n", str, len);
}
