#!/usr/bin/python3
""" Rectangle model """
from .base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the area of this rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ print the rectangle with # character """
        for row in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """ return a resume of this Rectangle instance """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.y, self.__width, self.__height)

    def display(self):
        """ print the rectangle with # character taking x
            and y into account """
        print("\n" * self.__y, end="")
        for row in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def update(self, *args, **kwargs):
        """ update an existing Rectagle instance """
        if kwargs is not None:
            for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value
        else:
            length = len(args)
            if (length > 0):
                self.id = args[0]
            if (length > 1):
                self.width = args[1]
            if (length > 2):
                self.height = args[2]
            if (length > 3):
                self.x = args[3]
            if (length > 4):
                self.y = args[4]

    def to_dictionary(self):
        return self.__dict__
