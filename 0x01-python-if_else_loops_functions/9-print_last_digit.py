#!/usr/bin/python3
def print_last_digit(number):
    n = number
    if n < 0:
        positive = n * -1
    else:
        positive = n
    rest = positive % 10
    print(rest, end='')
    return rest
