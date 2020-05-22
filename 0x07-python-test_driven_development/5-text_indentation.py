#!/usr/bin/python3
""" Text identation """


def text_indentation(text):
    """
    Write a function that prints a text with 2 new lines after each of these
    characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    chrs = ['.', '?', ':']
    spc = False
    for i in text:
        if spc is False:
            if i == ' ':
                continue
            else:
                print("{}".format(i), end="")
                spc = True
        else:
            if i in chrs:
                print("{}".format(i), end="\n\n")
                spc = False
            else:
                print("{}".format(i), end="")
