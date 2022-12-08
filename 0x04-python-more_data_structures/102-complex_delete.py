#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    val = []
    for i, v in a_dictionary.items():
        if v == value:
            val.append(i)
    if len(val) != 0:
        for j in range(len(val)):
            del a_dictionary[val[j]]

    return a_dictionary
