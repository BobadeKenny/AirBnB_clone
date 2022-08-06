#!/usr/bin/python3
"""Unittest for BaseModel class
"""
import os
import unittest
from datetime import datetime
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""
    def test_init(self):
        """Test initialization"""
        b1 = BaseModel()
        self.assertIs(type(b1), BaseModel)
        b1.name = "My First Model"
        b1.number = 89
        self.assertEqual(b1.name, "My First Model")
        self.assertEqual(b1.number, 89)
        self.assertIs(type(b1.id), str)
        self.assertIs(type(b1.created_at), datetime)
        self.assertIs(type(b1.updated_at), datetime)

    def test_str(self):
        """test string representation of class"""
        b2 = BaseModel()
        str_rep = "[{}] ({}) {}".format(b2.__class__.__name__,
                                        b2.id, b2.__dict__)
        self.assertEqual(str(b2), str_rep)

    def test_save(self):
        """test save method of BaseModel"""
        b3 = BaseModel()
        prev_updated = b3.updated_at
        time.sleep(1)
        b3.save()
        new_updated = b3.updated_at
        self.assertNotEqual(prev_updated, new_updated)

    def test_to_dict(self):
        """test dict representation of class"""
        b4 = BaseModel()
        class_dict = b4.to_dict()
        self.assertEqual(len(class_dict.keys()), 4)
        self.assertEqual(class_dict["__class__"], b4.__class__.__name__)
        self.assertIs(type(class_dict["created_at"]), str)
        self.assertIs(type(class_dict["updated_at"]), str)
