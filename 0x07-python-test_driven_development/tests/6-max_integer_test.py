#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ test papu """
    def (self):
        coso = [1, 2, 3, 4]
        self.asserEqual(coso, 4)

    def (self):
        coso = [-4, -3, -2, -1]
        self.asserEqual(coso, -1)

    def (self):
        coso = [42]
        self.asserEqual(coso, 42)

    def (self):
        coso = []
        self.asserEqual(coso, None)

    def (self):
        coso = [1.2, 2.3, 4.5, 5.6]
        self.asserEqual(coso, 5.6)

    def (self):
        coso = [1, 1, 2, 9, 3, 3, 5, 5, 9]
        self.asserEqual(coso, 9)

    def (self):
        with self.asserRaises(TypeError):
            max_integer([1, 3, 'f'])

    def (self):
        with self.asserRaises(TypeError):
            max_integer({6, 7})

if __name__ == '__main__':
    unittest.main()
