/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 17:28:11 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/28 17:28:20 by mpanzani         ###   ########.fr       */
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
	while (str[i] && str[i] != ' ' && str[i] != '\t' && str[i] != '\n')
		i++;
	return (i);
}

char	**ft_split(char *str)
{
	char	**result;
	int		i;
	int		j;
	int		len;

	result = malloc(sizeof(char *) * (count_words(str) + 1));
	if (!result)
		return (NULL);
	i = 0;
	j = 0;
	while (str[i])
	{
		if (str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
			i++;
		else
		{
			len = word_len(str + i);
			result[j] = malloc(sizeof(char) * (len + 1));
			if (!result[j])
				return (NULL);
			result[j][len] = '\0';
			len = 0;
			while (str[i] && str[i] != ' ' && str[i] != '\t' && str[i] != '\n')
			{
				result[j][len] = str[i];
				len++;
				i++;
			}
			j++;
		}
	}
	result[j] = NULL;
	return (result);
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
	return (0);
}
