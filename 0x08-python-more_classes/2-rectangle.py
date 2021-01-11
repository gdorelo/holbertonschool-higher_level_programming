#!/usr/bin/python3
'''Rectangle class'''


class Rectangle:
    '''what are these for? who knows'''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    '''getter width'''
    @property
    def width(self):
        return self.__width
    ''' setter width '''
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    '''getter height'''
    @property
    def height(self):
        return self.__height
    ''' setter height '''
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    '''return the rectangle's area'''
    def area(self):
        return self.__width * self.__height
    '''return the rectangle's perimeter'''
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
