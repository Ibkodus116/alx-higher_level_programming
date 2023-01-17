#!/usr/bin/python3

"""
Module for file opening
"""


def read_file(filename=""):
    """Function Opening a file for reading"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
