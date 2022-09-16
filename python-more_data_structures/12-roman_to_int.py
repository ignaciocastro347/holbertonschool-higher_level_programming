#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    rommap = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    values = list(map(lambda x: rommap[x], roman_string))
    values = [
        (x * -1)
        if i + 1 < len(values) and values[i + 1] > x
        else x for i, x in enumerate(values)
        ]
    return sum(values)
