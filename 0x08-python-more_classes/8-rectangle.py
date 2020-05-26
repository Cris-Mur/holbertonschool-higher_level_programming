#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ Rectangle definition """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """ width get """
    @property
    def width(self):
        return self.__width

    """ width set """
    @width.setter
    def width(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    """ height get """
    @property
    def height(self):
        return self.__height

    """ height set """
    @height.setter
    def height(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    """ area """
    def area(self):
        return (self.__width * self.__height)

    """ perimeter """
    def perimeter(self):
        if self.__width != 0 and self.height != 0:
            return ((self.__width * 2) + (self.height * 2))
        else:
            return 0

    """ str output """
    def __str__(self):
        stri = ""
        if self.__width != 0 and self.height != 0:
            for y in range(self.__height):
                for x in range(self.__width):
                    stri += str(self.print_symbol)
                if y < self.__height - 1:
                    stri += '\n'

        return stri

    """ output repr """
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    """ delete routine """
    def __del__(self):
        Rectangle.number_of_instances -= 1
        return print("Bye rectangle...")

    """ comparation instances """
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
