#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """what are these for? who knows"""
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        """ initiate rectangle"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
    @property
    def width(self):
        """getter width"""
        return self.__width
    @width.setter
    def width(self, value):
        """ setter width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    def area(self):
        """return the rectangle's area"""
        return self.__width * self.__height

    def perimeter(self):
        """return the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print rectangle"""
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

    def __repr__(self):
        """ roberto """
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        """ delete my balls """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """static method"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ equisde equisde """
        return Rectangle(size, size)
