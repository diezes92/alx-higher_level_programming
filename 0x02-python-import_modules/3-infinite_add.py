#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    lgt = len(sys.argv) - 1

    if lgt == 0:
        print("{}".format(sum))
    elif lgt >= 1:
        for i in range(1, lgt + 1, 1):
            sum = sum + int(sys.argv[i])
        print("{}".format(sum))
