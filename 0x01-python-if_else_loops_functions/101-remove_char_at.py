#!/usr/bin/python3
def remove_char_at(str, n):
    index = 0
    s = ''
    for i in str:
        if index != n:
            s += str[index]
        index += 1
    return (s)
