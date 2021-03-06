#!/usr/bin/python3
""" Rectangle Class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle definition inherit Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Fn area """
        return (self.__width * self.__height)

    def display(self):
        """ Display in a console """
        for y in range(0, self.__y):
            print()
        for y in range(0, self.__height):
            print((self.__x*' ')+(self.__width*"#"))

    def __str__(self):
        """ string display """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id,
            self.__x, self.__y,
            self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """ update routine"""
        agu = ("id", "width", "height", "x", "y")
        if args and len(args) != 0:
            for cso in range(len(args)):
                setattr(self, agu[cso], args[cso])
        elif kwargs:
            for key, vl in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, vl)

    def to_dictionary(self):
        """ dictionary repr """
        idx = {"id": self.id,
               "width": self.width,
               "height": self.height,
               "x": self.x,
               "y": self.y}
        return idx
