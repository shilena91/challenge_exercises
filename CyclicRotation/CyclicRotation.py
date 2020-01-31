# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    CyclicRotation.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: HoangPham <HoangPham@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/31 20:29:47 by HoangPham         #+#    #+#              #
#    Updated: 2020/01/31 21:12:35 by HoangPham        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def solution(A, K):
    if (len(A) == 0 or K < 0):
        return
    while (K > 0):
        lastItem = A.pop()
        A.insert(0, lastItem)
        K -= 1
    return (A)

A = list()
K = 3
solution(A, K)
print(A)
