#!/usr/bin/python3
""" check if is instance """


def inherits_from(obj, a_class):
    """ return true if obj is an instance of a class """
    return (isinstance(obj, a_class) and type(obj) != a_class)
