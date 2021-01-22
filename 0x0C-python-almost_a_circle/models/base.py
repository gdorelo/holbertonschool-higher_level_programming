#!/usr/bin/python3
''' Base class module '''


import json


class Base:
    ''' Base class '''
    __nb_objects = 0


    def __init__(self, id=None):
        ''' Initialization of Base class '''
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns the JSON string representation of list_dictionaries '''
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writed the json string representation of list_objs to a file '''
        filename = cls.__name__ + ".json"
        list_o = []
        if list_objs is not None:
            for i in list_objs:
                list_o.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_o))
