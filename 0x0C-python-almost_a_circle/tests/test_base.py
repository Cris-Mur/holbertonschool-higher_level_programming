#!/usr/bin/python3
""" Unit test Base class """
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class Testidcheck(unittest.TestCase):
    """ tests """

    def stup(self):
        """ for atributes """
        Base._Base__nb_objects = 0

    def test_arg(self):
        """ auto id """
        one = Base()
        self.assertEqual(one.id, 1)
        two = Base()
        self.assertEqual(two.id, 2)
        tre = Base()
        self.assertEqual(tre.id, 3)

    def test_none(self):
        """ auto id """
        one = Base(None)
        self.assertEqual(one.id, 4)
        two = Base(None)
        self.assertEqual(two.id, 5)
        tre = Base(None)
        self.assertEqual(tre.id, 6)

    def test_st_id(self):
        """ no auto id """
        one = Base(42)
        self.assertEqual(one.id, 42)
        two = Base(-64)
        self.assertEqual(two.id, -64)
        tre = Base()
        self.assertEqual(tre.id, 7)

if __name__ == '__main__':
    unittest.main()
