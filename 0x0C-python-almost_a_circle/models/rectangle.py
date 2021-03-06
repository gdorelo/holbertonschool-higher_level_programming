#!/usr/bin/python3
''' Rectangle class module, which inherits from Base '''


from models.base import Base


class Rectangle(Base):
    ''' Rectangle class '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Initializes a Rectangle '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @width.setter
    def width(self, value):
        ''' width setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        ''' height setter '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        ''' x setter '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        ''' y setter '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' returns the area of a rectangle '''
        return self.__width * self.__height

    def display(self):
        ''' prints the rectangle to stdout '''
        for i in range(self.y):
            print("")
        for j in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width)

    def __str__(self):
        ''' informal string representation of a rectangle '''
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        ''' updates rectangle's attributes '''
        atrs = ['id', 'width', 'height', 'x', 'y']
        if args and args[0] is not None:
            for i in range(len(args)):
                setattr(self, atrs[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle '''
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
