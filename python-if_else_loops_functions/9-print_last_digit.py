#!/usr/bin/python3
def print_last_digit(number):
    last_digit = int(abs(number)) % 10
    print(last_digit, end="")
    return last_digit
