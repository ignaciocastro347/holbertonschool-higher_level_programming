#!/usr/bin/python3
""" Unittest for Rectangle class """
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(1, 2, 3)
        self.r3 = Rectangle(1, 2, 3, 4)

    def test_init1(self):
        self.assertEqual(self.r1.to_dictionary(), {"id": 1, "width": 1, "height": 2, "x": 0, "y":0})

    def test_init2(self):
        self.assertEqual(self.r1.to_dictionary(), {"id": 1, "width": 1, "height": 2, "x": 0, "y":0})

    def test_init3(self):
        self.assertEqual(self.r1.to_dictionary(), {"id": 1, "width": 1, "height": 2, "x": 0, "y":0})

class TestRectangle(unittest.TestCase):
    def test_init(self):
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")