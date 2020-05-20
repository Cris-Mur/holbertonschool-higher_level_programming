#!/usr/bin/python3
""" Square class """


class Square:
    """ Define square size """
    def __init__(self, new_size=0):
        if type(new_size) == int:
            if new_size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = new_size
        else:
            raise TypeError("size must be an integer")
