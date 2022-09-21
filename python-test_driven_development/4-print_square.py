#!/usr/bin/python3
""" say my name module """


def print_square(size):
    """ function to print a square with # """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size == 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
