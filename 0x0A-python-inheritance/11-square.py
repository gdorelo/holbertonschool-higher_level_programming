#!/usr/bin/python3
"""Contains the class BaseGeometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """what are these for? who knows"""
    def __init__(self, size):
        """to initialize"""
        self.integer_validator("size", size)
        # ask why:
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculate area"""
        return self.__size * self.__size

    def __str__(self):
        """return info"""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
