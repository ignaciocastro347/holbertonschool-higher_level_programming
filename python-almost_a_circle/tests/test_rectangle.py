#!/usr/bin/python3
""" Unittest for Rectangle class """
import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """  TestRectangle class """
    def test_init1(self):
        """ test_init1 method """
        self.r1 = Rectangle(1, 2)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)

    def test_init2(self):
        """ test_init2 method """
        self.r2 = Rectangle(1, 2, 3)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 3)

    def test_init3(self):
        """ test_init3 method """
        self.r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(self.r3.width, 1)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 3)
        self.assertEqual(self.r3.y, 4)

    def test_init4(self):
        """ test_init4 method """
        self.r3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r3.width, 1)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 3)
        self.assertEqual(self.r3.y, 4)
        self.assertEqual(self.r3.id, 5)


class TestRectangleExceptions(unittest.TestCase):
    """  TestRectangleExceptions class """
    def test_init(self):
        """ test_init method """
        self.assertRaises(TypeError, Rectangle, "1", 2)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, "3")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

    def test_init2(self):
        """ test_init2 method """
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)


class TestRectangleArea(unittest.TestCase):
    """  TestRectangleArea class """
    def test_area(self):
        """ test_area method """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.area(), 2)


class TestRectangleStr(unittest.TestCase):
    """  TestRectangleStr class """
    def test_str(self):
        """ test_str method """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (5) 3/4 - 1/2")


class TestRectangleDisplay(unittest.TestCase):
    """  TestRectangleDisplay class """
    def test_display(self):
        """ test_display method """
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


class TestRectangleToDict(unittest.TestCase):
    """  TestRectangleToDict class """
    def test_to_dictionary(self):
        """ test_to_dictionary method """
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.to_dictionary(), {
            "id": 5,"width": 1,"height": 2,"x": 3,"y": 4})


class TestRectangleUpdate(unittest.TestCase):
    """  TestRectangleUpdate class """
    def test_update1(self):
        """ test_update1 method """
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(1, 2, 3, 4, 5)
        r1.update()
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    # def test_update2(self):
    #     """update() method with regular integer arguments passed"""
    #     self.r = Rectangle(1, 2, 3, 4, 5)
    #     self.r.update(89)
    #     self.assertEqual(self.r.id, 89)
    #     self.r.update(89, 1)
    #     self.assertEqual(self.r.width, 1)
    #     self.r.update(89, 1, 2)
    #     self.assertEqual(self.r.height, 2)
    #     self.r.update(89, 1, 2, 3)
    #     self.assertEqual(self.r.x, 3)
    #     self.r.update(89, 1, 2, 3, 4)
    #     self.assertEqual(self.r.y, 4)

    def test_update3(self):
        """update() method with dictionary type
        (**, key='value') argument passed"""
        self.r = Rectangle(10, 10, 10, 10, 10)
        self.r.update(**{'id': 89})
        self.assertEqual(self.r.id, 89)
        self.r.update(**{'id': 89, 'width': 1})
        self.assertEqual(self.r.width, 1)
        self.r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(self.r.height, 2)
        self.r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(self.r.x, 3)
        self.r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(self.r.y, 4)

    def test_create(self):
        """ test_create method """
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)


class TestRectSave2(unittest.TestCase):
    """save_to_file() method"""

    def test_save_to_file2(self):
        """save_to_file() method"""
        Rectangle.save_to_file([])
        with open('Rectangle.json') as file:
            self.assertEqual('[]', file.read())


class TestRectSave3(unittest.TestCase):
    """save_to_file() method"""

    def test_save_to_file3(self):
        """save_to_file() method"""
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 1)])
        with open('Rectangle.json') as file:
            self.assertEqual(
                '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]', file.read())