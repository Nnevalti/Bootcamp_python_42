# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdescham <vdescham@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 14:15:16 by vdescham          #+#    #+#              #
#    Updated: 2020/03/09 14:15:18 by vdescham         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

argv = sys.argv

if len(argv) < 3 or len(argv) > 3 or not argv[1].isdigit() or not argv[2].isdigit():
	if len(argv) > 3 :
		print("\033[0;31;1mInputError:\033[0;37;0m too many argument\n")
	elif len(argv) == 3 and (not argv[1].isdigit() or not argv[2].isdigit()) :
		print("\033[0;31;1mInputError:\033[0;37;0m only number\n")
	print("\033[0;32;1mUsage:\033[0;33;0m python operations.py <number1> <number2>")
	print("\033[0;33;1mExample:\033[0;37;0m")
	print("\tpython operations.py 10 3")
	exit()

n1, n2 = argv[1], argv[2]

print("\033[0;37;1mSum:\033[0;37;0m\t\t", int(n1) + int(n2))
print("\033[0;37;1mDifference:\033[0;37;0m\t", int(n1) - int(n2))
print("\033[0;37;1mProduct:\033[0;37;0m\t", int(n1) * int(n2))
if int(n2) == 0 :
	print("\033[0;37;1mQuotient:\033[0;37;0m\t ERROR (div by zero)")
	print("\033[0;37;1mRemainder:\033[0;37;0m\t ERROR (modulo by zero)")
else :
	print("\033[0;37;1mQuotient:\033[0;37;0m\t", int(n1) / int(n2))
	print("\033[0;37;1mRemainder:\033[0;37;0m\t", int(n1) % int(n2))
