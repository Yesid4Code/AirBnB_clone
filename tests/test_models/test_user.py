#!/usr/bin/python3
"""
Test User  containing classes to test on the Place class:
    * Style.
    * Documentation.
    * Functionality.
"""
import unittest
import pep8
from models import user
from models.user import User


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/user.py'
        file2 = 'tests/test_models/test_user.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(user.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(user.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)


class TestPlace(unittest.TestCase):
    """ New class to test class Amenity"""

    def setUp(self):
        """ Setting up"""
        self.new = User()

    def tearDown(self):
        """ Cleaning up after each test"""
        del self.new

    def test_is_instance(self):
        """ Check if attributes are instances"""
        self.assertTrue(type(self.new) is User)

    def test_if_str(self):
        """Check if the attribute is a str"""
        self.assertTrue(type(self.new.email) is str)
        self.assertTrue(type(self.new.password) is str)
        self.assertTrue(type(self.new.first_name) is str)
        self.assertTrue(type(self.new.last_name) is str)

if __name__ == '__main__':
    unittest.main()
