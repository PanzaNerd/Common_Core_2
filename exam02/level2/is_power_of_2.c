/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   is_power_of_2.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mpanzani <mpanzani@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 16:48:28 by mpanzani          #+#    #+#             */
/*   Updated: 2026/05/28 17:02:14 by mpanzani         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>

int	    is_power_of_2(unsigned int n)
{
	if(n == 0)
		return(0);
	if((n & (n - 1)) == 0)
		return(1);
	return(0);
}

int main(void)
{
	printf("%d\n", is_power_of_2(32));
	return(0);
}
