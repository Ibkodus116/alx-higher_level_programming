#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    elif len(my_list) == 1:
        return my_list[0]

    l_num = my_list[0]
    for i in my_list:
        if i > l_num:
            l_num = i
    return l_num
