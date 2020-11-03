#!/usr/bin/python3
"""
Test for pep8
"""
import unittest
import pep8
from models.base_model import BaseModel
from models.user import User


class Testpep8(unittest.TestCase):
    """
    Test of file pep8
    """
    def test_pep8_conformance_base_model(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_pep8_conformance_user(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_pep8_conformance_init(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/__init__.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_pep8_conformance_file_storage(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_pep8_conformance_console(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")
