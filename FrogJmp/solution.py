# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: HoangPham <HoangPham@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/06 21:26:51 by HoangPham         #+#    #+#              #
#    Updated: 2020/02/06 21:45:01 by HoangPham        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def solution(X, Y, D):
    if (X > Y):
        return (0)
    distance = Y - X
    jump = int(distance / D)
    if (distance % D == 0):
        return (jump)
    else:
        return (jump + 1)
