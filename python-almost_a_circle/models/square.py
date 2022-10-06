#!/usr/bin/python3
""" Rectangle model """
from .rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return a resume of this Square instance """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be > 0")
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """ update an existing Square instance """
        if kwargs is not None:
            for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self.width = self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value
        else:
            length = len(args)
            if (length > 0):
                self.id = args[0]
            if (length > 1):
                self.width = self.height = args[1]
            if (length > 2):
                self.x = args[2]
            if (length > 3):
                self.y = args[3]
