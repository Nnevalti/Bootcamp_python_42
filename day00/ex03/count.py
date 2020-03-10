# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdescham <vdescham@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 13:20:11 by vdescham          #+#    #+#              #
#    Updated: 2020/03/09 13:20:13 by vdescham         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

argv = sys.argv

def text_analyzer(*str) :
	"""This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""

	if len(str) > 1 :
		print("ERROR")
		return
	elif len(str) == 0 :
		print("What is the text to analyze ?")
		text = input();
	elif str[0] == "" :
		print("Text is empty")
		return
	else :
		text = str[0]
	count, upper, lower, space, punct = 0, 0, 0, 0, 0
	for i in text :
		count += 1
		if i.isupper() : upper += 1
		elif i.islower() : lower += 1
		elif i.isspace() : space += 1
		elif i in string.punctuation : punct += 1
	print("The text contains %d characters:\n" % count)
	print("- %d upper letters\n" % upper)
	print("- %d lower letters\n" % lower)
	print("- %d punctuation marks\n" % punct)
	print("- %d spaces\n" % space)
