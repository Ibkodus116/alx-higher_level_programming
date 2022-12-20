#!/usr/bin/python3
def safe_print_integer(value):
    try:
        v = int(value)
        print("{:d}".format(v))

    except:
        return False

    return True
