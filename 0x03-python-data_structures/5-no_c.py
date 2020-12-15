#!/usr/bin/python3
def no_c(my_string):
    list = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            list += i
    return list
