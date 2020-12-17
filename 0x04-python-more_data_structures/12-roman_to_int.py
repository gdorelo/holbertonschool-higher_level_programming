#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if type(roman_string) != str:
        return num
    if roman_string is None:
        return num
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list(roman_string).reverse()
    c = len(roman_string)
    for i in range(c):
        if i < c - 1 and roman[roman_string[i]] < roman[roman_string[i + 1]]:
            num -= roman[roman_string[i]]
        else:
            num += roman[roman_string[i]]
    return num
