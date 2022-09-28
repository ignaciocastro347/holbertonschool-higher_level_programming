#!/usr/bin/python3
""" Student module """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict = self.__dict__
        if (type(attrs) == list
            and all(type(x) == str for x in attrs)):
            return { key: dict[key] for key in set(attrs) & set(dict.keys()) }
        return dict
