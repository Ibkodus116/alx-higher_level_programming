#!/usr/bin/python3
def safe_print_integer(value):
    try:
        v = int(value)
        print(v)

    except ValueError:
        return False

    return True
