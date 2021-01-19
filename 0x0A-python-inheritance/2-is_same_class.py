#!/usr/bin/python3
"""This module contains is_same_class"""


def is_same_class(obj, a_class):
    """returns true if obj is an instance of class a_class, otherwise false"""
    return (type(obj) == a_class)
