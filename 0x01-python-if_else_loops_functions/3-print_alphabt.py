#!/usr/bin/python3
for c in range(97, 123):
    if ord('q') != c and ord('e') != c:
        print("{}".format(chr(c)), end="")
