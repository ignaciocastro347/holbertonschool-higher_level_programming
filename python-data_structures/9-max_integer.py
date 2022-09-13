#!/usr/bin/python3
def max_integer(my_list=[]):
    max = None
    for i, num in enumerate(my_list):
        if i == 0 or num > max:
            max = num
    return max
