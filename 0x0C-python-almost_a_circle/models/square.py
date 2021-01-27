#!/usr/bin/python3
''' Square class module, which inherits from Rectangle and Base '''


from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square class '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' initialize a Square '''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        ''' size getter '''
        return self.width

    @size.setter
    def size(self, value):
        ''' size setter '''
        self.width = value
        self.height = value

    def __str__(self):
        ''' string representation of a square '''
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        ''' updates a square '''
        atrs = ['id', 'size', 'x', 'y']
        if args and args[0] is not None:
            for i in range(len(args)):
                setattr(self, atrs[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        ''' returns the dictionary representation of a square '''
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
