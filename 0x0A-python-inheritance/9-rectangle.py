#!/usr/bin/python3
""" BaseGeometry Class """


class BaseGeometry:
    "Class base for check inputs for geometryclasses"
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (value.__class__ != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:} must be greater than 0".format(name))

""" Rectangle Class """


class Rectangle(BaseGeometry):
    """ Rectangle Class """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {:d}/{:d}".format(self.__class__.__name__, self.__width,
                                       self.__height)
