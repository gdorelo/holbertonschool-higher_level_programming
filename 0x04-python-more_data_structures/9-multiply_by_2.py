#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for key in a_dictionary:
        key, new[key] = key, a_dictionary[key] * 2
    return new
