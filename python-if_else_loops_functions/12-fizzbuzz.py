#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15:
            print("Fizz", end=" ")
        elif i % 5:
            print("Buzz", end=" ")
        else:
            print("", end=" ")
