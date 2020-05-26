#!/usr/bin/python3
class Rectangle:
    """ def init function """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ def property width get """
    @property
    def width(self):
        return self.__width

    """ def width set """
    @width.setter
    def width(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    """ def height get """
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

    """ def area function """
    def area(self):
        return (self.__width * self.__height)

    """ def perimeter function """
    def perimeter(self):
        if self.__width != 0 and self.height != 0:
            return ((self.__width * 2) + (self.height * 2))
        else:
            return 0
