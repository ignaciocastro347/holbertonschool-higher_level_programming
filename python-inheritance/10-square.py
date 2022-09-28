#!/usr/bin/python3
""" Square module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        self.integer_validation("size", size)
        self._size = size

    def area(self):
        return self._size * self._size
