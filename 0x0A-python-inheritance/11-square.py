#!/usr/bin/python3
""" inherits rectangle """

Rectangle = __import__('9-rectangle').Rectangle

""" Square Class """


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Area Function """
        return super().area()

    def __str__(self):
        """ str repr """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
