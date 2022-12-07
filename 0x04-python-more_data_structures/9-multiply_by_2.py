#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    my_keys = list(a_dictionary)
    my_val = list(a_dictionary.values())

    for i in range(len(my_keys)):
        new_dict[my_keys[i]] = my_val[i] * 2

    return new_dict
