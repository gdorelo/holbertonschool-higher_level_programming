#!/usr/bin/python3
"""Contains the class BaseGeometry"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validation"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value is <= 0:
            raise ValueError("<name> must be greater than 0")
