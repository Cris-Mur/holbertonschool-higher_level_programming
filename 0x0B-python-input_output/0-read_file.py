#!/urs/bin/python3
""" function that open a text file and print this is stdout """


def read_file(filename=""):
    """ read file function """
    with open(filename, mode='r', encoding="utf-8") as coso:
        print(coso.read(), end='')
