#!/usr/bin/python3
"""
Test Filestorage containing classes to test on the FileStorage class:
    * Style.
    * Documentation.
    * Functionality.
"""
import pep8
import unittest
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/file_storage.py'
        file2 = 'tests/test_models/test_engine/test_file_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)


class TestFileStorage(unittest.TestCase):
    """ Check for functionality of File_Storage class. """
    def setUp(self):
        """ Method to set the star point. """
        self.model0 = FileStorage()

    def tearDown(self):
        """ . """
        del self.model0

    def test_is_instance(self):
        """ Check if a variable is an instance. """
        self.assertIsInstance(self.model0, FileStorage)

    def test_all(self):
        """ Test if the method return a dictionary correctly. """
        dic = self.model0.all()
        self.assertEqual(type(dic), dict)
        self.assertIs(dic, self.model0._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
