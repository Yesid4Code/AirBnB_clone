#!/usr/bin/python3
""" Model to test the console. """
import pep8
import unittest
from console import HBNBCommand


class TestPep8Console(unittest.TestCase):
    """ Check for pep8 validation. """
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


class TestConsole(unittest.TestCase):
    """ Check for functionality. """
    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('console.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('console.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('console.py', os.X_OK)
        self.assertTrue(exe)
