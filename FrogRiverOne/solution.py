# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: HoangPham <HoangPham@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/07 21:04:56 by HoangPham         #+#    #+#              #
#    Updated: 2020/02/07 23:36:45 by HoangPham        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
This solution get 100% correctness but 0% performance on Codility :(
'''

def solution(X, A):
    if (X <= 0 or len(A) == 0):
        return (-1)
    position = 0
    i = 1
    if A[0] <= X:
        position += 1
        if position == X:
            return (0)
    for nb in A[1:]:
        if nb <= X and nb not in A[:i]:
            position += 1
        if position == X:
            return (i)
        i += 1
    return (-1)

A = range(1, 100001)
print(solution(100000, A)) 

