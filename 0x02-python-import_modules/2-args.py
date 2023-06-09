#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lgt = len(sys.argv) - 1

    if lgt == 0:
        print("{} arguments.".format(lgt))
    elif lgt == 1:
        print("{} argument:".format(lgt))
    else:
        print("{} arguments:".format(lgt))

    if lgt == 1:
        print("{}: {}".format(lgt, sys.argv[1]))
    elif lgt > 1:
        for i in range(1, lgt + 1, 1):
            print("{}: {}".format(i, sys.argv[i]))
