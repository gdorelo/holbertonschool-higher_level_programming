#!/usr/bin/python3
"""print a list"""


class MyList(list):
    '''class'''

    def __init__(self):
        """initialize"""
        super().__init__()

    def print_sorted(self):
        """print the list"""
        print(sorted(self))
