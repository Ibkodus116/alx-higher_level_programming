#!/usr/bin/python3

"""
Module for file opening
"""
def read_file(filename="", encoding="utf-8"):
    """Function Opening a file for reading"""
    with open(filename) as f:
        print(f.read())
