#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        num = fct(*args)
    except Exception as i:
        stderr.write("Exception: {}\n".format(i))
        return None
    return num
