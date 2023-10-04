#!/usr/bin/python3
for i in range(100):
    print("{}".format(format(i, '02')), end="")
    if i != 99:
        print(", ", end="")
