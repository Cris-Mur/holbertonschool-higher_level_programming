#!/usr/bin/python3
""" module divide matrix """


def matrix_divided(matrix, div):
    """
    function that divide all values matrix
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(err)
    for prt in matrix:
        if type(prt) is not list:
            raise TypeError(err)
        for coso in prt:
            if type(coso) is not int and type(coso) is not float:
                raise TypeError(err)

    if len(set([len(i) for i in matrix])) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div <= 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x/div, 2) for x in y] for y in matrix]
