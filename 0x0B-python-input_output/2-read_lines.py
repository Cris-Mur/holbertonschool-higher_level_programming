#!/usr/bin/python3
""" read per lines """


def read_lines(filename="", nb_lines=0):
    """ only lines """
    with open(filename, encoding='utf-8') as coso:
        if (nb_lines != 0):
            for line in coso:
                if (nb_lines != 0):
                    print(line, end="")
                else:
                    break
                nb_lines -= 1
        else:
            for line in coso:
                print(line, end="")
    return nb_lines
