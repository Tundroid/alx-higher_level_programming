#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d = [key for key in a_dictionary.keys() if a_dictionary[key] == value]
    for key in d:
        del a_dictionary[key]
    return a_dictionary
