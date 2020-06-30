#!/usr/bin/python3
"""
Test BaseModel  containing classes to test on the BassModel class:
    * Functionality.
    * Style.
    * Documentation.
"""
import os
import pep8
import unittest
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


class TestBaseModel(unittest.TestCase):
    """ Check for functionality. """
    def setUp(self):
        """ Method to set the star point. """
        self.model0 = BaseModel()
        self.model1 = BaseModel()

    def tearDown(self):
        """ . """
        del self.model0
        del self.model1

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(exe)

    def test_is_instance(self):
        """ Check if a variable is an instance. """
        self.assertIsInstance(self.model0, BaseModel)

    def test_id(self):
        """ Check if id of a instance is a string or equal to another one. """
        self.assertNotEqual(self.model0.id, self.model1.id)
        self.assertEqual(type(self.model0.id), str)

    def test_save(self):
        """ Test if the method 'save' is working. """
        old_created_at = self.model0.created_at
        old_updated_at = self.model0.updated_at
        self.model0.save()
        new_created_at = self.model0.created_at
        new_updated_at = self.model0.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)

    def test_to_dict(self):
        """ Test if the method return a dictionary correctly. """
        form = "%Y-%m-%dT%H:%M:%S.%f"
        dic = self.model0.to_dict()
        self.assertEqual(dic["__class__"], "BaseModel")
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(dic["created_at"],
                         self.model0.created_at.strftime(form))
        self.assertEqual(dic["updated_at"],
                         self.model0.updated_at.strftime(form))

if __name__ == '__main__':
    unittest.main()

# Test
# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_base_model.py
