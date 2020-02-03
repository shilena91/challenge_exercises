# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: HoangPham <HoangPham@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/31 21:25:29 by HoangPham         #+#    #+#              #
#    Updated: 2020/02/03 23:22:38 by HoangPham        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
This solution solves 100% correctness but only 25% performance test on Codility
It took too long time when array's length are 999,999
'''

def solution(A):
    i = 0
    while (len(A) > 1):
        j = i + 1
        while (j < len(A)):
            if (A[i] == A[j]):
                del A[i]
                del A[j - 1]
                i = -1
                break
            j += 1
        i += 1
    return A[0]

A = [1, 3, 1, 3, 5, 2, 5, 2, 6, 7, 6, 7, 8, 9, 8, 9, 10, 0, 10]
print(solution(A))
                     