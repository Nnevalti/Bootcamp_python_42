# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdescham <vdescham@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 11:54:37 by vdescham          #+#    #+#              #
#    Updated: 2020/03/09 11:59:49 by vdescham         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
argv = sys.argv

def whois(num) :
   if num % 2 == 1 :
       print("I'm odd.");
   elif num == 0:
       print("I'm Zero.")
   else :
	   print("I'm even.")

if (len(argv)) == 2 and argv[1].isdigit() :
	whois(int(argv[1]));
else :
	print("ERROR")
