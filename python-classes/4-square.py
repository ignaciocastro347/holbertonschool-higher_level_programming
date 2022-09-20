#!/usr/bin/python3
""" 1-square module """


class Square:
    """ class Square """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def x(self, size):
        self.__size = size

    def area(self):
        return self.__size * self.__size
