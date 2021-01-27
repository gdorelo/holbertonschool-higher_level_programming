#!/usr/bin/python3
''' Tests for Square class '''

import unittest
import pep8
import inspect
import json
from models import square
from models.base import Base
Square = square.Square


class TestSquareDocs(unittest.TestCase):
    '''Tests the Square class' style and documentation'''
    @classmethod
    def setUpClass(cls):
        '''Set up for the doc tests'''
        cls.sq_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_pep8_conformance_square(self):
        '''Test that models/square.py conforms to PEP8.'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_rectangle(self):
        '''Test that tests/test_models/test_square.py conforms to PEP8.'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        '''Tests for the presence of a module docstring'''
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstring(self):
        '''Tests for the presence of a class docstring'''
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstrings(self):
        '''Tests for the presence of docstrings in all functions'''
        for func in self.sq_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestSquare(unittest.TestCase):
    '''Test the functionality of the Square class'''
    @classmethod
    def setUpClass(cls):
        '''set up the tests'''
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)
        cls.s3 = Square(4, 5, 6)
        cls.s4 = Square(7, 8, 9, 10)