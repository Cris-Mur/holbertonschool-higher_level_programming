#!/usr/bin/python3
""" Find peak in a list """


def find_peak(list_of_integers):
    ''' finding peak '''
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
