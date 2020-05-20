#!/usr/bin/python3
class Square:
    __size = 0
    def __init__(self, new_size=0):
        if type(new_size) == int:
            if new_size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = new_size
        else:
            raise TypeError("size must be an integer")
