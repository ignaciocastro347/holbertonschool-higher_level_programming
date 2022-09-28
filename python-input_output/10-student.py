#!/usr/bin/python3
""" Student module """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) == list
            and all(type(x) == str for x in attrs)):
            return { key: self.__dict__[key] for key in attrs }
        return self.__dict__
