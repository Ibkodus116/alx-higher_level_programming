#!/usr/bin/python3
for i in range(1, 80):
    if i % 10 > i / 10:
        print(f"{i:02d}", end=", ")
print("89")
