#!/usr/bin/python3
""" class_to_json module """
import json


def class_to_json(obj):
    """ class_to_json function """
    return obj.__dict__
