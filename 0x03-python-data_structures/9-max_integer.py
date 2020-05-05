#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list != []:
        max_doge = my_list[0]
        for steps in my_list:
            if max_doge < steps:
                max_doge = steps
    return max_doge if my_list != [] else None
