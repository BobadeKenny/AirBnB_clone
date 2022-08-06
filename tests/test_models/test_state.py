#!/usr/bin/python3
"""Unittest for User
"""
import os
import unittest
from datetime import datetime
import time
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""
    def test_init(self):
        """Test initialization"""
        s1 = State()
        self.assertIs(type(s1), State)
        self.assertIsInstance(s1, BaseModel)
        self.assertTrue(hasattr(s1, "name"))
        self.assertIs(type(s1.id), str)
        self.assertIs(type(s1.created_at), datetime)
        self.assertIs(type(s1.updated_at), datetime)

    def test_str(self):
        """test string representation of class"""
        s2 = State()
        str_rep = "[{}] ({}) {}".format(s2.__class__.__name__,
                                        s2.id, s2.__dict__)
        self.assertEqual(str(s2), str_rep)

    def test_save(self):
        """test save method of BaseModel"""
        s3 = State()
        prev_updated = s3.updated_at
        time.sleep(1)
        s3.save()
        new_updated = s3.updated_at
        self.assertNotEqual(prev_updated, new_updated)

    def test_to_dict(self):
        """test dict representation of class"""
        s4 = State()
        class_dict = s4.to_dict()
        self.assertEqual(len(class_dict.keys()), 4)
        self.assertEqual(class_dict["__class__"], s4.__class__.__name__)
        self.assertIs(type(class_dict["created_at"]), str)
        self.assertIs(type(class_dict["updated_at"]), str)
