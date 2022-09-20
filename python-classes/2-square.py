#!/usr/bin/python3
""" 1-square module """


class Square:
    """ class Square """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("bar must be set to an integer")
        self.__size = size
