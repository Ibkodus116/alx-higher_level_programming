#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "CD": 400,
        "DC": 600,
        "DCCC": 800,
        "CM": 900,
        "XL": 40,
        "LX": 60,
        "LXX": 70,
        "LXXX": 80,
        "XC": 90,
        "IV": 4,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9
        }
    i = 0
    num = 0
    rom_list = list(rom)
    roman = roman_string
    for i in roman_string:
        if i in rom_list:
            num += rom[i]
    return num
