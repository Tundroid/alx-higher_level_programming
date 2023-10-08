#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print("{}".format(matrix[row][col]), end="")
            print("", end=" " if col != len(matrix[row]) - 1 else "\n")
