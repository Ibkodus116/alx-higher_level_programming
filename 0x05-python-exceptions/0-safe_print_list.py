#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        while num < x:
            print(f"{my_list[num]}", end="")
            num += 1
    except IndexError:
        print("\n")
        return num

    print("\n")
    return num
