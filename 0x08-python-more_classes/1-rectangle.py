#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:
    """ Rectangle Class init function"""
    def __init__(self, width=0, height=0):
        if type(width) == int:
            if width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = width
        else:
            raise TypeError("width must be an integer")

        if type(height) == int:
            if height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = height
        else:
            raise TypeError("height must be an integer")

    """ Property width get """
    @property
    def width(self):
        return self.__width

    """ Define setter width """
    @width.setter
    def width(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    """ property height get """
    @property
    def height(self):
        return self.__height

    """ def height set """
    @height.setter
    def height(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")
