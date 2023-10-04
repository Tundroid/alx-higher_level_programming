#!/usr/bin/python3
for i in range(25, -1, -1):
    if (i % 2 == 0):
        print(chr(ord('A') + i), end="")
    else:
        print(chr(ord('a') + i), end="")
