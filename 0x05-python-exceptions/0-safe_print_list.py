#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    w = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            w += 1
        except:
            break
    print()
    return w
