#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = (tuple_a + ((0,) * (2 - len(tuple_a))))[:2]
    tuple_b = (tuple_b + ((0,) * (2 - len(tuple_b))))[:2]
    return tuple(map(sum, zip(tuple_a, tuple_b)))
