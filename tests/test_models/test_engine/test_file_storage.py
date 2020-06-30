#!/usr/bin/python3
"""
Test Filestorage containing classes to test on the FileStorage class:
    * Style.
    * Documentation.
    * Functionality.
"""
import os
import pep8
import unittest
from datetime import datetime
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
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)


class TestFileStorage(unittest.TestCase):
    """ Check for functionality of File_Storage class. """
    def setUp(self):
        """ setUp. """
        self.storage_1 = FileStorage()

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(exe)

    def test_instance(self):
        """check if obj is an instance of BaseModel"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def check_all(self):
        """ Checks a correct dictionary """
        dic = self.storage_1.all()
        self.assertEqual(type(dic), dict)
        self.assertIs(dic, self.storage_1._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
