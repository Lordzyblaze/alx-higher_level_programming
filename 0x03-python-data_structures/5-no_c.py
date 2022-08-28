#!/usr/bin/python3
def no_c(my_string):
    listofchars = list(my_string)
    for lens in listofchars:
        if lens == 'c' or lens == 'C':
            listofchars.remove(lens)
    return("".join(listofchars))
