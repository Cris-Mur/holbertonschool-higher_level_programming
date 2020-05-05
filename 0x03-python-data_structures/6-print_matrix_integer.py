#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for level in matrix:
        for box in level:
            print("{:d}".format(box), end="")
            if box != level[-1]:
                print(" ", end="")
        print("")
