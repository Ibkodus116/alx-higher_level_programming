#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    arg = len(argv) - 1
    if arg == 3:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print(f"{a} + {b} = {add(a, b)}")
        elif argv[2] == "-":
            print(f"{a} - {b} = {sub(a, b)}")
        elif argv[2] == "*":
            print(f"{a} * {b} = {mul(a, b)}")
        elif argv[2] == "/":
            print(f"{a} / {b} = {div(a, b)}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
