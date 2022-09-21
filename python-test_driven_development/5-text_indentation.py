#!/usr/bin/python3
""" say my name module """


def text_indentation(text):
    """ function to add and print '\n\n' up and down when '.', ':' or '?' is found """
    if type(text) != str:
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n").replace("?", "?\n\n").replace(":", ":\n\n") 
    if text.endswith("\n\n"):
        text = text[:-2]
    print(text, end="")
