#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        lent = len(i) - 1
        for j in i:
            if j != i[lent]:
                print("{:d}".format(j), end=" ")
            if j == i[lent]:
                print("{:d}".format(j), end="")
        print()
