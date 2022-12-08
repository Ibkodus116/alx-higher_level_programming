#!/usr/bin/python3
def weight_average(my_list=[]):
    mul = 0
    add = 0
    for i in range(len(my_list)):
        mul += my_list[i][0] * my_list[i][1]
        add += my_list[i][1]
    return mul / add
