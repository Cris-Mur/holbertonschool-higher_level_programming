#!/usr/bin/python3
"""" BaseGeometry Class """
class BaseGeometry:
    "Class base for check inputs for geometryclasses"
    def __init__(self):
        pass

    """ area function """
    def area(self):
        raise Exception("area() is not implemented")

    """ integer validator function """
    def integer_validator(self, name, value):
        if (value.__class__ != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:} must be greater than 0".format(name))
