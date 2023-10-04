#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c = ord(c)
        if c >= 97 and c <= 123:
            c = chr(ord('A') + (c - ord('a')))
        else:
            c = chr(c)
        print("{}".format(c), end="")
    print()
