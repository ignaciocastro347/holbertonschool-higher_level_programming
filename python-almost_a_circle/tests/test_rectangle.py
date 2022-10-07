#!/usr/bin/python3
""" Unittest for Rectangle class """
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init1(self):
        self.r1 = Rectangle(1, 2)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)

    def test_init2(self):
        self.r2 = Rectangle(1, 2, 3)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 3)

    def test_init3(self):
        self.r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(self.r3.width, 1)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 3)
        self.assertEqual(self.r3.y, 4)


class TestRectangle(unittest.TestCase):
    def test_init(self):
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")