# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdescham <vdescham@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 15:13:47 by vdescham          #+#    #+#              #
#    Updated: 2020/03/09 15:13:51 by vdescham         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

t = (19,42,21,4,5,6,78,98,45)

str = "The %d numbers are: " % len(t)
for i in range (0, len(t) - 1) :
	str += "%d, " % t[i]
str += "%d" % t[len(t) - 1]
print(str)