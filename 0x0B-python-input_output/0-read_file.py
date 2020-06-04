#!/urs/bin/python3
""" function that open a text file and print this is stdout """


def read_file(filename=""):
    """ read file function """
    coso = open(filename)
    print(coso.read(), end='')
