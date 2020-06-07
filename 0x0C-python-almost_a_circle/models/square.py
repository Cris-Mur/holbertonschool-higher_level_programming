#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Def Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ init fn """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ str over write """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id,
            self.x, self.y, self.size)
