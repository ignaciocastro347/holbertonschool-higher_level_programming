#!/usr/bin/python3
""" write_file module """


def write_file(filename="", text=""):
    """ write_file function """
    with open(filename, "w", encoding="utf-8") as f:
        length_text = f.write(text)
    f.close()
    return length_text
