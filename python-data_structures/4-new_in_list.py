#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = list(my_list)
    if (my_list and idx in range(0, len(my_list))):
        copy_list[idx] = element
    return copy_list
