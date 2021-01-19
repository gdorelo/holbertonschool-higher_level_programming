#!/usr/bin/python3
"""inherits_from  function"""


def inherits_from(obj, a_class):
    """True if obj is an instance or inherited from a_class, if not, False"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
