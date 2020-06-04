#!/usr/bin/python3
"""  """


def write_file(filename="", text=""):
    """  """
    with open(filename, mode='w', encoding='utf-8') as coso:
        if text != "":
            return coso.write(text)
        return 0
