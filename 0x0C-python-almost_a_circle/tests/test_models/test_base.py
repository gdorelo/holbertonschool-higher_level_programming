#!/usr/bin/python3
''' Tests for Base class '''

import unittest
import inspect
import pep8
import json
from models import base
Base = base.Base


class TestBaseDocs(unittest.TestCase):
    '''Tests for checking the documentation and style of Base class'''
    @classmethod
    def setUpClass(cls):
        '''Set-up for doc tests'''
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8_conformance_base(self):
        '''Test that models/base.py complies with PEP8.'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        '''Test that tests/test_models/test_base.py complies with PEP8.'''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        '''Tests for module docstring'''
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        '''Tests for Base class docstring'''
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        '''Tests for presence of docstrings in all of the functions'''
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBase(unittest.TestCase):
    '''Tests to check basic functionality of Base class'''
    def test_too_many_args(self):
        '''test too many args to init'''
        with self.assertRaises(TypeError):
            b = Base(1, 1)
