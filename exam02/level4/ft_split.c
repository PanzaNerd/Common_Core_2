/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: matthias <matthias@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 20:19:10 by mpanzani          #+#    #+#             */
/*   Updated: 2026/06/10 20:22:04 by matthias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

int count_words(char *str)
{
	int i = 0;
	int count = 0;

	while(str[i])
	{
		if(str[i] != ' ' && str[i] != '\t' && str[i] != '\n')
			if(i == 0 || str[i - 1] == ' ' || str[i - 1] == '\t' || str[i - 1] == '\n')
				count++;
		i++;	
	}
	return(count);
}

int word_len(char *str, int i)
{
	int len = 0;

	while(str[i + len] && str[i + len] != ' ' && str[i + len] != '\t' && str[i + len] != '\n')
		len++;
	return(len);
}

char *copy_word(char *str, int i, int len)
{
	char *word;
	int x = 0;
	
	word = malloc(sizeof(char) * (len + 1));
	if(!word)
		return(NULL);
	while(x < len)
	{
		word[x] = str[i + x];
		x++;
	}
	word[x] = '\0';
	return(word);
}

char **ft_split(char *str)
{
	char **arr;
	int count;
	int i = 0;
	int len = 0;
	int n = 0;
	
	count = count_words(str);
	
	arr = malloc(sizeof(char *) * (count + 1));

	if(!arr)
		return(NULL);

	while(str[i])
	{
		while (str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
            i++;
		if (str[i] == '\0')
            break;
		len = word_len(str, i);
		arr[n] = copy_word(str, i, len);
		i = i + len;
		n++;
	}
	arr[n] = NULL;
	return(arr);
}

int main(void)
{
	char **arr;
	char str[] = "ciao come stai";
	int i = 0;

	arr = ft_split(str);
	while(arr[i])
	{
		printf("%s", arr[i]);
		printf("\n");
		i++;
	}
	return(0);
}


/*
1. Quante parole ci sono? (count_words)
2. Allocare array di puntatori(ognuno punta a una stringa) char*
3. i è la posizione nella stringa originaria, n è lo slot dell'array
4. While: scorre la stringa saltando gli spazi, controlla se è finita ('\0')
5. While: misura len di ogni parola con word_len
6. While: copia la parola in uno degli n slot dell'array con copy_word
7. While: avanzamento degli indici
8. Chiudere l'array con l'ultimo slot NULL
9. Ritorna l'array di puntatori->stringhe
*/
