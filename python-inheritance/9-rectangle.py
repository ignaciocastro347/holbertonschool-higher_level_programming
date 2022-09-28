#!/usr/bin/python3
""" Rectangle module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

    def __repr__(self):
        print("[Rectangle] {}/{}".format(self._width, self._height))

    def __str__(self):
        return "[Rectangle] {}/{}".format(self._width, self._height)

    def area(self):
        return self._width * self._height
