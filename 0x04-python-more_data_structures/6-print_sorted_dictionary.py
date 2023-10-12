#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())
    [print("{}: {}".format(key, a_dictionary[key])) for key in keys]
