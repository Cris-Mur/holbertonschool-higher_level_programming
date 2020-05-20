#!/usr/bin/python3
""" Square class """


class Square:
    """ Define square init with pos"""
    def __init__(self, new_size=0, new_position=(0, 0)):
        self.__size = new_size
        self.__position = new_position

    """ Define property position """
    @property
    def position(self):
        return self.__position

    """ Define setter position """
    @position.setter
    def position(self, value):
        if (type(new_position[0]) == int and type(new_position[1]) == int or
            type(new_position) == tuple and len(new_position) == 2 and
                new_position[0] > 0 and new_position[1] > 0):
            self.__position = new_position
        else:
            raise TypeError("position must be a tuple or 2 positive integers")

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

    """ Define square area """
    def area(self):
        return self.__size**2

    """ Define square my_print """
    def my_print(self):
        if self.__size == 0:
            print()
            return
        for py in range(self.__position[1]):
            print()
        for y in range(self.__size):
                print("{:s}{:s}".format(' ' * self.__position[0],
                                        '#' * self.__size))
