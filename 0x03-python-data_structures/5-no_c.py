#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        new_string += "" if char in ["c", "C"] else char
    return new_string
