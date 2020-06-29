#!/usr/bin/python3
"""Test module"""


import unittest
import pep8
from models import state
from models.state import State


class TestAmenity(unittest.TestCase):
    """New class to test class Amenity"""

    def setUp(self):
        """Setting up"""
        self.new = State()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.new

    def test_is_instance(self):
        """Check if attributes are instances"""
        self.assertTrue(type(self.new) is State)

    def test_if_str(self):
        """Check if the attribute is str"""
        self.assertTrue(type(self.new.name) is str)


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/state.py'
        file2 = 'tests/test_models/test_state.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(state.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(state.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)
if __name__ == '__main__':
    unittest.main()
