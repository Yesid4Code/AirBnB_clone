#!/usr/bin/python3
"""
Test Place  containing classes to test on the Place class:
    * Style.
    * Documentation.
    * Functionality.
"""
import unittest
import pep8
from models import place
from models.place import Place


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/place.py'
        file2 = 'tests/test_models/test_place.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(place.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(place.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)


class TestPlace(unittest.TestCase):
    """ New class to test class Amenity"""

    def setUp(self):
        """ Setting up"""
        self.new = Place()

    def tearDown(self):
        """ Cleaning up after each test"""
        del self.new

    def test_is_instance(self):
        """ Check if attributes are instances"""
        self.assertTrue(type(self.new) is Place)

    def test_if_str(self):
        """Check if the attribute is a str"""
        self.assertTrue(type(self.new.city_id) is str)
        self.assertTrue(type(self.new.user_id) is str)
        self.assertTrue(type(self.new.name) is str)
        self.assertTrue(type(self.new.description) is str)

    def test_if_int(self):
        """ Check if the attribute is a int. """
        self.assertTrue(type(self.new.number_rooms) is int)
        self.assertTrue(type(self.new.number_bathrooms) is int)
        self.assertTrue(type(self.new.max_guest) is int)
        self.assertTrue(type(self.new.price_by_night) is int)

    def test_if_float(self):
        """ Check if the attributes is a float. """
        self.assertTrue(type(self.new.latitude) is float)
        self.assertTrue(type(self.new.longitude) is float)

    def test_if_list(self):
        """ Test if the attribute is a list. """
        self.assertEqual(type(self.new.amenity_ids), list)
