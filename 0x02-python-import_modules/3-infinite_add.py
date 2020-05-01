#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)
    if size <= 1:
        print("0")
    else:
        sum = 0
        for i in sys.argv[1:]:
            sum += int(i)

        print("{:d}".format(sum))
