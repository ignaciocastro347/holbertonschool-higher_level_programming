#!/usr/bin/python3
""" Unittest for Rectangle class """
import unittest
import sys
from io import StringIO
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

    def test_init4(self):
        self.r3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r3.width, 1)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 3)
        self.assertEqual(self.r3.y, 4)
        self.assertEqual(self.r3.id, 5)



class TestRectangleExceptions(unittest.TestCase):
    def test_init(self):
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

    def test_init2(self):
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

class TestRectangleArea(unittest.TestCase):
    def test_area(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.area(), 2)

class TestRectangleStr(unittest.TestCase):
    def test_str(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (5) 3/4 - 1/2")

class TestRectangleDisplay(unittest.TestCase):
    def test_display(self):
        stdout = StringIO()
        sys.stdout = stdout
        r1 = Rectangle(2, 1, 0, 0)
        r2 = Rectangle(2, 1, 1)
        r3 = Rectangle(2, 1, 1, 1)
        r1.display()
        self.assertEqual(stdout.getvalue(), "##\n")
        r2.display()
        self.assertEqual(stdout.getvalue(), "##\n ##\n")
        r3.display()
        self.assertEqual(stdout.getvalue(), "##\n ##\n\n ##\n")



