#!/usr/bin/python3
""" first doctest python """


def add_integer(a, b=98):
    """
    This function add two integers that only can be an integer or float
    "a" and "b" must be first casted to integers if they are float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(a) is float:
        a = int(a)
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif type(b) is float:
        b = int(b)

    return int(a + b)
