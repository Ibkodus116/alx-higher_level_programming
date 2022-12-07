#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    d_key = list(a_dictionary)

    if key in d_key:
        del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary
