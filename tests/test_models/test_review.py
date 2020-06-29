#!/usr/bin/python3
"""Test module"""


import unittest
import pep8
from models import review
from models.review import Review


class TestCity(unittest.TestCase):
    """New class to test class City"""

    def setUp(self):
        """Set instance"""
        self.new = Review()

    def tearDown(self):
        """Cleaning up after each test"""
        del self.new

    def test_is_instance(self):
        """Check if the instance belongs to class City"""
        self.assertTrue(type(self.new) is Review)

    def test_id(self):
        """Check if state_id is a string"""
        self.assertTrue(type(self.new.place_id) is str)

    def test_user(self):
        """Check if name is a str"""
        self.assertTrue(type(self.new.user_id) is str)

    def test_text(self):
        """Check if name is a str"""
        self.assertTrue(type(self.new.text) is str)


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/review.py'
        file2 = 'tests/test_models/test_review.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(review.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(review.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)

if __name__ == '__main__':
    unittest.main()
