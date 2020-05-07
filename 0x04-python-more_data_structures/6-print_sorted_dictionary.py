#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for step in sorted([cheat for cheat in a_dictionary]):
        print("{}: {}".format(step, a_dictionary[step]))
