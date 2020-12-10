#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    c = len(argv) - 1
    if c == 0:
        print("0 arguments.")
    else:
        if c == 1:
            print("{} argument:".format(c))
            print("{}: {}".format(c, argv[c]))
        else:
            print("{} arguments:". format(c))
            for x in range(1, c + 1):
                print("{}: {}". format(x, argv[x]))
