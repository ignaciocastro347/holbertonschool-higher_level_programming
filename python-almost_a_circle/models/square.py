#!/usr/bin/python3
""" Rectangle model """
from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return a resume of this Square instance """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.__x, self.y, self.__width)
