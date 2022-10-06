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
        return "[]" if list_dictionaries is None else json.dumps(list_dictionaries)
