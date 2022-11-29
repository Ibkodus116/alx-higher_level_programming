#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)
        #print(num)
        if num >= 97 and num <= 122:
            num = num - 32
            
        print(f"{num:c}", end="")
    print("")
        

