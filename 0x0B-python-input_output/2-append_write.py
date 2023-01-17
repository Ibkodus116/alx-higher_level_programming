#!/usr/bin/python3

"""
Module for appending a file
"""

def append_write(filename="", text=""):
    with open(filename, 'a') as f:
        return f.write(text)