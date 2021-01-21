#!/usr/bin/python3
''' Student class '''


class Student:
    ''' and this student class? '''

    def __init__(self, first_name, last_name, age):
        ''' Initialization for student class'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Get the dict of a Student ;) '''
        return self.__dict__
