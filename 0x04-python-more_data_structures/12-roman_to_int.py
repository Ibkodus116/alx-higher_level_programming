#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if roman_string is None:
        return 0

    rom = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
        }
    i = 0
    num = 0
    rom_list = list(rom)

    while i < len(roman_string):
        two = roman_string[i:i+2]
        if two in rom_list:
            num += rom[two]
            i += 1
        else:
            if roman_string[i] not in rom_list:
                return 0
            num += rom[roman_string[i]]
        i += 1
    return num
