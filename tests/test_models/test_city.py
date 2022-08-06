#!/usr/bin/python3
"""Unittest for City
"""
import os
import unittest
from datetime import datetime
import time
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""
    def test_init(self):
        """Test initialization"""
        user1 = City()
        self.assertIs(type(user1), City)
        self.assertIsInstance(user1, BaseModel)
        self.assertTrue(hasattr(user1, "name"))
        self.assertTrue(hasattr(user1, "state_id"))
        self.assertIs(type(user1.id), str)
        self.assertIs(type(user1.created_at), datetime)
        self.assertIs(type(user1.updated_at), datetime)

    def test_str(self):
        """test string representation of class"""
        u2 = City()
        str_rep = "[{}] ({}) {}".format(u2.__class__.__name__,
                                        u2.id, u2.__dict__)
        self.assertEqual(str(u2), str_rep)

    def test_save(self):
        """test save method of BaseModel"""
        u3 = City()
        prev_updated = u3.updated_at
        time.sleep(1)
        u3.save()
        new_updated = u3.updated_at
        self.assertNotEqual(prev_updated, new_updated)

    def test_to_dict(self):
        """test dict representation of class"""
        u4 = City()
        class_dict = u4.to_dict()
        self.assertEqual(len(class_dict.keys()), 4)
        self.assertEqual(class_dict["__class__"], u4.__class__.__name__)
        self.assertIs(type(class_dict["created_at"]), str)
        self.assertIs(type(class_dict["updated_at"]), str)
