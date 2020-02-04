# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: HoangPham <HoangPham@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/05 00:16:34 by HoangPham         #+#    #+#              #
#    Updated: 2020/02/05 00:27:13 by HoangPham        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def solution(A):
    firstPart = A[0]
    secondPart = sum(A[1:])
    minDifference = abs(firstPart - secondPart)
    for index in range(1, len(A) - 1):
        firstPart += A[index]
        secondPart -= A[index]
        if abs(firstPart - secondPart) < minDifference:
            minDifference = abs(firstPart - secondPart)
    return (minDifference)
    