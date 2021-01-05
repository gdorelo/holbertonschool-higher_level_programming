#!/usr/bin/python3
'''square class'''


class Square:
    '''what are these for? who knows'''
    def __init__(self, size=0,  position=(0, 0)):
        self.size = size
        self.position = position
    '''getter size'''
    @property
    def size(self):
        return self.__size
    ''' setter size '''
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    '''getter position'''
    @property
    def position(self):
        return self.__position
    '''setter position'''
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    '''return's square area'''
    def area(self):
        return self.__size ** 2
    '''print square'''
    def my_print(self):
        if self.__size is 0:
            print()
            return
        if self.__position:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            print("".join(" " for j in range(self.__position[0])), end="")
            print("".join("#" for j in range(self.__size)))
