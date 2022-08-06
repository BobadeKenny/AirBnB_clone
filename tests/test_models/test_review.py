#!/usr/bin/python3
"""Unittest for Review
"""
import os
import unittest
from datetime import datetime
import time
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""
    def test_init(self):
        """Test initialization"""
        r1 = Review()
        self.assertIs(type(r1), Review)
        self.assertIsInstance(r1, BaseModel)
        self.assertTrue(hasattr(r1, "place_id"))
        self.assertTrue(hasattr(r1, "user_id"))
        self.assertTrue(hasattr(r1, "text"))
        self.assertIs(type(r1.id), str)
        self.assertIs(type(r1.created_at), datetime)
        self.assertIs(type(r1.updated_at), datetime)

    def test_str(self):
        """test string representation of class"""
        u2 = Review()
        str_rep = "[{}] ({}) {}".format(u2.__class__.__name__,
                                        u2.id, u2.__dict__)
        self.assertEqual(str(u2), str_rep)

    def test_save(self):
        """test save method of BaseModel"""
        u3 = Review()
        prev_updated = u3.updated_at
        time.sleep(1)
        u3.save()
        new_updated = u3.updated_at
        self.assertNotEqual(prev_updated, new_updated)

    def test_to_dict(self):
        """test dict representation of class"""
        u4 = Review()
        class_dict = u4.to_dict()
        self.assertEqual(len(class_dict.keys()), 4)
        self.assertEqual(class_dict["__class__"], u4.__class__.__name__)
        self.assertIs(type(class_dict["created_at"]), str)
        self.assertIs(type(class_dict["updated_at"]), str)
