# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: HoangPham <HoangPham@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/04 21:25:54 by HoangPham         #+#    #+#              #
#    Updated: 2020/02/04 22:18:47 by HoangPham        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def solution(A):
    A.sort()
    if (len(A) == 0):
        return (1)
    if (A[0] != 1):
        return (1)
    if (A[-1] != len(A) + 1):
        return (len(A) + 1)
    i = 0
    while (i < len(A) - 1):
        A[i] += 1
        if (A[i] != A[i + 1]):
            return A[i]
        i += 1

A = [1,2,6,4,3,7]
print(solution(A))
