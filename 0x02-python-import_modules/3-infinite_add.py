#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1
    result = 0
    if argc == 0:
        print(result)
    else:
        for i in range(1, argc + 1):
            result += int(argv[i])
        print(result)
