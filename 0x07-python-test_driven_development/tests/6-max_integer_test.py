#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ test papu """
    def test_normal(self):
        coso = [1, 2, 3, 4]
        self.assertEqual(max_integer(coso), 4)

    def test_negative(self):
        coso = [-4, -3, -2, -1]
        self.assertEqual(max_integer(coso), -1)

    def test_alone(self):
        coso = [42]
        self.assertEqual(max_integer(coso), 42)

    def test_none(self):
        coso = []
        self.assertEqual(max_integer(coso), None)

    def test_float(self):
        coso = [1.2, 2.3, 4.5, 5.6]
        self.assertEqual(max_integer(coso), 5.6)

    def test_reppit(self):
        coso = [1, 1, 2, 9, 3, 3, 5, 5, 9]
        self.assertEqual(max_integer(coso), 9)

    def test_tERR_l(self):
        with self.assertRaises(TypeError):
            max_integer([1, 3, 'f'])

    def test_tERR_s(self):
        with self.assertRaises(TypeError):
            max_integer({6, 7})

if __name__ == '__main__':
    unittest.main()
