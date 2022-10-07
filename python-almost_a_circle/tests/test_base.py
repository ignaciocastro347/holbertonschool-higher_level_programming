#!/usr/bin/python3
""" Unittest for Base class """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        self.b = Base()
    
    def test_init1(self):
        self.assertEqual(self.b.id, 1)
    
    def test_init2(self):
        self.assertEqual(self.b.id, 2)
    
    def test_init3(self):
        self.assertEqual(self.b.id, 3)

class TestRepeatedBase(unittest.TestCase):
    def setUp(self):
        self.b = Base(1)

    def test_init(self):
        self.assertEqual(self.b.id, 1)

class TestToJsonString(unittest.TestCase):
    def setUp(self):
        self.b = Base()

    def test_to_json_string(self):
        self.assertEqual(self.b.to_json_string(None), "[]")
