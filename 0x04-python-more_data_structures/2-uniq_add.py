#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    for i in my_list:
        my_set.add(i)

    return sum(my_set)
