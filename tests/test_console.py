#!/usr/bin/python3
"""Unittest for Console
"""
import os
import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test Command Intepreter"""
    def test_prompt(self):
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")
