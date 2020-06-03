#!/usr/bin/python3
""" MyList class """


class MyList(list):
    """ The class parameter is a list """

    def print_sorted(self):
        """ print sorted  """
        print(sorted(self))
