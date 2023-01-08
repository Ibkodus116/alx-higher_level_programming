#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(12,45)
# print("")
print_square(4)
print("")
print_square(6)
print("")
print_square(2)
print("")
try:
    print_square(0.5)
except Exception as f:
    print(f)
print("")