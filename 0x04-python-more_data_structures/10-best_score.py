#!/usr/bin/python3
def best_score(a_dictionary):
    num = 0
    if not a_dictionary:
        return None
    else:
        d_keys = list(a_dictionary)
        d_val = list(a_dictionary.values())
        largest = d_val[0]
        for i in d_val:
            if i > largest:
                largest = i
        idx = d_val.index(largest)
        return d_keys[idx]
