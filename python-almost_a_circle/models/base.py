#!/usr/bin/python3
""" Base model """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return the JSON string repr of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_json_file function """
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                json.dump(list_objs, f)
