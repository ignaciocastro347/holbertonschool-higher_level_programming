#!/usr/bin/python3
from copy import copy


def new_in_list(my_list, idx, element):
    copy_list = my_list.copy()
    if my_list:
        copy_list[idx] = element
    return copy_list
