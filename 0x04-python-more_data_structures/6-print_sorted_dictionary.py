#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_sort = sorted(a_dictionary)
    for i in my_sort:
        print(f"{i}: {a_dictionary[i]}")
