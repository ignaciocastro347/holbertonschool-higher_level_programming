#!/usr/bin/python3
""" 1-square module """


class Square:
    """ class Square """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

        if len(tuple(position)) != 2:
            raise TypeError("position must be a tuple of 2 positive integers") 
        self.__position = position

    @property
    def size(self):
        return self.__size
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
    def position(self, position):
        if len(tuple(position)) != 2:
            raise TypeError("position must be a tuple of 2 positive integers") 
        self.__position = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        print("\n" * (self.__position[1] - 1))        
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
