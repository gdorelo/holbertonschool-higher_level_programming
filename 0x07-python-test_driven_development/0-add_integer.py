#!/usr/bin/python3
'''
This module defines a function called add_integer
'''


def add_integer(a, b=98):
    '''
    a function that returns two integers
    '''
    if type(a) is int or type(a) is float:
        pass
    else:
        raise TypeError("a must be an integer")
    if type(b) is int or type(b) is float:
        pass
    else:
        raise TypeError("b must be an integer")
    return int(a + b)
