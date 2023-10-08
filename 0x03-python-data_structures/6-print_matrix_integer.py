#!/usr/bin/python3
def print_matrix_integer(m=[[]]):
    for row in range(len(m)):
        for col in range(len(m[row])):
            print("{:d}".format(m[row][col]), end="")
            print("{}".format(" " if col != len(m[row]) - 1 else "\n"), end="")
