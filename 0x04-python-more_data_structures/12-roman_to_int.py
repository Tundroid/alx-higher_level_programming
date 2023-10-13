#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    if roman_string and isinstance(roman_string, str):
        rom_numerals = {'I': 1, 'V': 5, 'X': 10,
                        'L': 50, 'C': 100, 'D': 500,
                        'M': 1000}
        i = len(roman_string) - 1
        while i >= 0:
            right = rom_numerals[roman_string[i]]
            sum += right
            i -= 1
            if i > 0:
                left = rom_numerals[roman_string[i]]
                sum += -left if right > left else left
                i -= 1
    return sum
