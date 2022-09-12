#!/usr/bin/python3
def no_c(my_string):
    return "".join([
        (char if (char != 'c' and char != 'C') else "") for char in my_string
        ])
