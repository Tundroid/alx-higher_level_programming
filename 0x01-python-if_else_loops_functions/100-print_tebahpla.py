#!/usr/bin/python3
for i in range(25, -1, -1):
    if (i % 2 == 0):
        c = chr(ord('A') + i)
    else:
        c = chr(ord('a') + i)
    print(c, end="")
