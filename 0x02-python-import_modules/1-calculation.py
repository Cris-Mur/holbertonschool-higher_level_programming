#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div

    tools = [add, sub, mul, div]
    sing = "+-*/"

    for i in range(len(sing)):
        print("{:d} {} {:d} = {:d}".format(a, sing[i], b, tools[i](a, b)))
