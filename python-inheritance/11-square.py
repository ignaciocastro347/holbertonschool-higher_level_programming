#!/usr/bin/python3
""" Square module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        self.integer_validator("size", size)
        self._size = size

    def __repr__(self):
        print("[Square] {}/{}".format(self._size, self._size))

    def __str__(self):
        return "[Square] {}/{}".format(self._size, self._size)

    def area(self):
        return self._size * self._size
