#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if "+" in operator:
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif "-" in operator:
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif "*" in operator:
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    elif "/" in operator:
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
