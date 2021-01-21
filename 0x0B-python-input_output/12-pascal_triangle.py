#!/usr/bin/python3
''' pascal_triangle function, with the purpose of: NULL '''
import math


def combination(n, r):
    ''' Helper function '''
    return int((math.factorial(n)) / ((math.factorial(r)) *
                                      math.factorial(n - r)))


def pascal_triangle(n):
    ''' Print the triangle '''
    if n <= 0:
        return []

    result = []
    for count in range(n):
        tmp = []
        for element in range(count + 1):
            tmp.append(combination(count, element))
        result.append(tmp)
    return result
