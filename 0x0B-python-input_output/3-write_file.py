#!/usr/bin/python3
""" write """


def write_file(filename="", text=""):
    """ write file """
    with open(filename, mode='w', encoding='utf-8') as coso:
        if text != "":
            return coso.write(text)
        return 0
