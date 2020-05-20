#!/usr/bin/python3
""" Square class """


class Square:
    """ Define square size init """
    def __init__(self, new_size=0):
        if type(new_size) == int:
            if new_size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = new_size
        else:
            raise TypeError("size must be an integer")

    """ Define square area """
    def area(self):
        return self.__size**2

    """ Define property size """
    @property
    def size(self):
        return self.__size

    """ Define setter size """
    @size.setter
    def size(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    """ Define square my_print """
    def my_print(self):
        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print()

        if self.__size == 0:
            print()
