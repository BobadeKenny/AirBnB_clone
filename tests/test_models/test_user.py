#!/usr/bin/python3
"""Unittest for User
"""
import os
import unittest
from datetime import datetime
import time
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""
    def test_init(self):
        """Test initialization"""
        user1 = User()
        self.assertIs(type(user1), User)
        self.assertIsInstance(user1, BaseModel)
        self.assertTrue(hasattr(user1, "email"))
        self.assertTrue(hasattr(user1, "password"))
        self.assertTrue(hasattr(user1, "first_name"))
        self.assertTrue(hasattr(user1, "last_name"))
        self.assertIs(type(user1.id), str)
        self.assertIs(type(user1.created_at), datetime)
        self.assertIs(type(user1.updated_at), datetime)

    def test_str(self):
        """test string representation of class"""
        u2 = User()
        str_rep = "[{}] ({}) {}".format(u2.__class__.__name__,
                                        u2.id, u2.__dict__)
        self.assertEqual(str(u2), str_rep)

    def test_save(self):
        """test save method of BaseModel"""
        u3 = User()
        prev_updated = u3.updated_at
        time.sleep(1)
        u3.save()
        new_updated = u3.updated_at
        self.assertNotEqual(prev_updated, new_updated)

    def test_to_dict(self):
        """test dict representation of class"""
        u4 = User()
        class_dict = u4.to_dict()
        self.assertEqual(len(class_dict.keys()), 4)
        self.assertEqual(class_dict["__class__"], u4.__class__.__name__)
        self.assertIs(type(class_dict["created_at"]), str)
        self.assertIs(type(class_dict["updated_at"]), str)
