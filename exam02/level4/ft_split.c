/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 17:28:11 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/02 20:29:36 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

static int	count_words(char *str)
{
	int	i;
	int	count;
	int	in_word;

	i = 0;
	count = 0;
	in_word = 0;

	while (str[i])
	{
		if (str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
			in_word = 0;
		else if (in_word == 0)
		{
			in_word = 1;
			count++;
		}
		i++;
	}
	return (count);
}

static int	word_len(char *str)
{
	int	i;

	i = 0;
	while (str[i]
		&& str[i] != ' '
		&& str[i] != '\t'
		&& str[i] != '\n')
		i++;
	return (i);
}

char	**ft_split(char *str)
{
	char	**res;
	int		i;
	int		j;
	int		k;
	int		len;

	res = malloc(sizeof(char *) * (count_words(str) + 1));
	if (!res)
		return (NULL);

	i = 0;
	j = 0;

	while (str[i])
	{
		while (str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
			i++;

		if (str[i])
		{
			len = word_len(str + i);

			res[j] = malloc(sizeof(char) * (len + 1));
			if (!res[j])
				return (NULL);

			k = 0;
			while (k < len)
			{
				res[j][k] = str[i];
				k++;
				i++;
			}

			res[j][k] = '\0';
			j++;
		}
	}

	res[j] = NULL;
	return (res);
}

int	main(void)
{
	char	**res;
	int		i;

	res = ft_split("  hello   world  foo  ");

	i = 0;
	while (res[i])
	{
		printf("[%s]\n", res[i]);
		i++;
	}
}
