#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (number * -1) % 10 if number < 0 else number % 10
last_digit = (last_digit * -1) if number < 0 else last_digit


print(f"Last digit of {number} is {last_digit}", end="")
if (last_digit > 5):
    print(f" and is greater than 5")
elif (last_digit == 0):
    print(f" and is zero")
else:
    print(f" and is less than 6 and not 0")
