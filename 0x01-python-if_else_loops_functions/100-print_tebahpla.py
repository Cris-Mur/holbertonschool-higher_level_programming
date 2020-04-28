#!/usr/bin/python3
a = 0
for i in range(0, 26):
    if a != 0:
        print("{:c}".format(90-i), end="")
        a = 0
    else:
        print("{:c}".format(122-i), end="")
        a = 1
