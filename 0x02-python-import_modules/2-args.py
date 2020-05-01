#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)

    print("{} argument".format(size - 1) if size == 2
          else "{} arguments".format(size - 1), end=".\n" if size == 1
          else ":\n")

    size = size - 1

    for i in range(1, size + 1):
        print("{}: {}".format(i, sys.argv[i]))
