#!/usr/bin/python3
"""
Module handling write function

"""


def write_file(filename="", text=""):
    """Funcion writting a file"""
    with open(filename, "w") as f:
        return f.write(text)
