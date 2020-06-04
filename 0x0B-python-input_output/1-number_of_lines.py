#!/usr/bin/python3
"""  """


def number_of_lines(filename=""):
    """  """
    line_n = 0
    with open(filename, encoding='utf-8') as coso:
        for line in coso:
            line_n += 1
    return line_n
