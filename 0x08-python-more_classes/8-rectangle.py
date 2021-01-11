#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """what are these for? who knows"""
    number_of_instances = 0
    print_symbol = '#'
    """ initiate rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
    """getter width"""
    @property
    def width(self):
        return self.__width
    """ setter width """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """getter height"""
    @property
    def height(self):
        return self.__height
    """ setter height """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """return the rectangle's area"""
    def area(self):
        return self.__width * self.__height
    """return the rectangle's perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
    """print rectangle"""
    def __str__(self):
        my_rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return my_rectangle
        for s in range(self.__height):
            my_rectangle += str(self.print_symbol)
            for t in range(self.__width - 1):
                my_rectangle += str(self.print_symbol)
            if s < self.__height - 1:
                my_rectangle += "\n"
        return my_rectangle
    """ roberto """
    def __repr__(self):
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)
    """ delete my balls """
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    """static method"""
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
