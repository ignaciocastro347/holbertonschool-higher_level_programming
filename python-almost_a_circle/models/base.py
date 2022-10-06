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
        """ save_to_json function """
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                str = "["
                for idx, obj in enumerate(list_objs):
                    if idx != 0:
                        str += ", "
                    str += cls.to_json_string(obj.to_dictionary())
                str += "]"
                f.write(str)

    @staticmethod
    def from_json_string(json_string):
        """ return the list of the JSON string """
        if (json_string is None or json_string == ""):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        "return an instance wit all attributes already set"
        if cls.__name__ == 'Rectangle':
            obj = cls(10, 10)
        elif cls.__name__ == 'Square':
            obj = cls(10)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ return a list of instances """
        filename = cls.__name__ + '.json'
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            file_contents = file.read()
        instances = cls.from_json_string(file_contents)
        lst = []
        for dict in instances:
            lst.append(cls.create(**dict))
        return lst
