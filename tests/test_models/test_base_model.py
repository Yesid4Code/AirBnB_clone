#!/usr/bin/python3
"""
Test BaseModel  containing classes to test on the BassModel class:
    * Functionality.
    * Style.
    * Documentation.
"""
import unittest
import pep8
from datetime import datetime
from models import base_model
from models.base_model import BaseModel


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


class TestBaseModel():
    """
    Class containing methods to test on BaseModel class:
    """
    pass


# Test
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_base.py
