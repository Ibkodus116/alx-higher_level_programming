#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        #print("{:d}".format(9))
        pass
    else:
        new_list = my_list.copy()
        new_list.reverse()
        for i in new_list:
            print("{:d}".format(i))
