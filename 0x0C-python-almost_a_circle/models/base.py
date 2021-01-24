#!/usr/bin/python3
''' Base class module '''


import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the JSON string representation json_string '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, new_list):
        ''' writes the json string representation of new_list to a file '''
        filename = cls.__name__ + ".json"
        jsonString = []
        if new_list is not None:
            for i in new_list:
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

    @classmethod
    def save_to_file_csv(cls, new_list):
        ''' serializes a list of Rectangles/Squares to csv '''
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as csvfile:
            csv_write = csv.writer(csvfile, delimiter=',')
            if cls.__name__ == "Rectangle":
                for obj in new_list:
                    csv_write.writerow([obj.id, obj.width,
                                        obj.height,
                                        obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in new_list:
                    csv_write.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        ''' classmethod load_from_file '''
        filename = cls.__name__ + ".csv"
        new_list = []
        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(args[0]),
                                      "size": int(args[1]),
                                      "x": int(args[2]),
                                      "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    new_list.append(obj)
        except:
            pass
        return new_list
