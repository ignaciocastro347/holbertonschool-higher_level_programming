#!/usr/bin/python3
def pow(a, b):
    if a == 0 or b == 0:
        return 1
    res = a
    for i in range(1, abs(b)):
        res *= a
    if b < 0:
        res = 1 / res
    return res
