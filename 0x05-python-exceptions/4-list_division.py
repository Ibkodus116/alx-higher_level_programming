#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    num = 0
    my_list = []
    try:
        for x in range(list_length):
            try:
                num = my_list_1[x] / my_list_2[x]
                my_list.append(num)
            except TypeError:
                print("wrong type")
                my_list.append(0)
                pass
            except ZeroDivisionError:
                my_list.append(0)
                print("division by 0")
                pass
            except IndexError:
                my_list.append(0)
                print("out of range")
                pass
    finally:
        return(my_list)
