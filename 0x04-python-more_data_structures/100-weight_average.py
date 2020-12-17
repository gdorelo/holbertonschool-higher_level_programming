#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        some = sum([x * y for x, y in my_list])
        return some/sum([y for x, y in my_list])
    return 0
