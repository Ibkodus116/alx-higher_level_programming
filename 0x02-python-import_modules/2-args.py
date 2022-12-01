#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print(f"{len(argv) - 1} arguments:")
    for i in range(len(argv)):
        if i != 0:
            print(f"{i}: {argv[i]}")
