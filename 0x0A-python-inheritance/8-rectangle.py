#!/usr/bin/python3
"""Contains the class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """what are these for? who knows"""
    def __init__(self, width, height):
        '''initialize'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
