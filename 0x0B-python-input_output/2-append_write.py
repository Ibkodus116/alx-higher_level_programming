#!/usr/bin/python3

"""
Module for appending a file
"""


def append_write(filename="", text=""):
    """Function Appending to a text"""

    with open(filename, 'a') as f:
        return f.write(text)
