#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = [False if step % 2 != 0 else True for step in my_list]
    return new
