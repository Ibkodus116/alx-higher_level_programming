#!/usr/bin/python3
def no_c(my_string):
    s = ""
    idx = 0
    for i in my_string:
        if i[idx] != "c" and i[idx] != "C":
            s += i[idx]
    return(s)
