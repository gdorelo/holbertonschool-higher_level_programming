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

    def from_json_string(json_string):
        ''' returns the list of the JSON string representation json_string '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the json string representation of list_objs to a file '''
        filename = cls.__name__ + ".json"
        jsonString = []
        if list_objs is not None:
            for i in list_objs:
                jsonString.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(jsonString))

    @classmethod
    def create(cls, **dictionary):
        ''' returns an instance with all of the attributes set '''
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        list_ = []
        try:
            with open(filename, 'r') as f:
                list_ = cls.from_json_string(f.read())
            for i, e in enumerate(list_):
                list_[i] = cls.create(**list_[i])
        except:
            pass
        return list_
