#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        y = 1
        for z in x:
            if y == len(x):
                print("{:d}".format(z), end="")
            else:
                print("{:d}".format(z), end=" ")
            y = y + 1
        print()
