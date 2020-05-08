#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) == False or roman_string is None:
        return 0

    rever=''.join(reversed(roman_string))
    roman={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0

    for x in rever:
        sum = sum + roman.get(x)

    return sum
