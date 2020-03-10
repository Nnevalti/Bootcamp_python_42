# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdescham <vdescham@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/09 11:09:33 by vdescham          #+#    #+#              #
#    Updated: 2020/03/09 11:50:28 by vdescham         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

argv = sys.argv
new_string = ''
i = len(argv) - 1
while i > 0 :
    j = len(argv[i]) - 1
    while j >= 0 :
        if (argv[i][j].isupper()) :
            new_string += argv[i][j].lower()
        else :
            new_string += argv[i][j].upper()
        j -= 1
    i -= 1
    if (i > 0) :
        new_string += ' ';
print(new_string)
