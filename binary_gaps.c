/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   binary_gaps.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hopham <hopham@student.hive.fi>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/27 17:48:36 by hopham            #+#    #+#             */
/*   Updated: 2019/11/27 19:44:04 by hopham           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*
**	function solution(), given a p integer N, returns the length of its longest binary gap.
**	The function should return 0 if N doesn't contain a binary gap.
**	A binary gap within a positive integer N is any maximal sequence of consecutive zeros
**	that is surrounded by ones at both ends in the binary representation of N.
**	For example, given N = 1041 the function should return 5, because N has binary representation 10000010001
**	so its longest binary gap is of length 5. Given N = 32 the function should return 0,
**	because N has binary representation '100000' and thus no binary gaps.
*/

#include <stdio.h>

int	bits = 0;
int	max = 0;

void	binary(int N)
{
	if (N > 1)
		binary(N / 2);
	if (N % 2 == 0)
	{
		bits += 1;
		return ;
	}
	if (max < bits)
		max = bits;
	bits = 0;
}

int	solution(int N)
{
	binary(N);
	return (max);
}

int	main(void)
{
	int	i;

	i = solution(529);
	printf("%i", i);
}
