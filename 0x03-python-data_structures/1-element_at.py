#!/usr/bin/python3
def element_at(my_list, idx):
    lent = len(my_list)
    if idx > lent or idx < 0:
        return "None"
    else:
        return my_list[idx]
