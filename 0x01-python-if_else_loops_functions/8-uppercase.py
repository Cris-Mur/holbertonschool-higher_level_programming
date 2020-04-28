#!/usr/bin/python3
def uppercase(str):
    for i in str + "\n":
        ch = ord(i)
        if ch >= 97 and ch <= 122:
            print("{}".format(chr(ch - 32)), end="")
        else:
            print("{}".format(chr(ch)), end="")
