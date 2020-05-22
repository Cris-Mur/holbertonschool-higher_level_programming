#!/usr/bin/python3
""" Print Square """


def print_square(size):
    """
    this function print a square by input size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        print("{}".format('#' * size))
