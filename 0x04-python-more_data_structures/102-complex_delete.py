#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = []
    for word in a_dictionary:
            if a_dictionary[word] == value:
                new.append(word)
    for delete in new:
        a_dictionary.pop(delete)
    return a_dictionary
