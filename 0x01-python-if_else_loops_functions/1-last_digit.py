#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if n < 0:
    numberpos = n * -1
else:
    numberpos = n
r = numberpos % 10
if n < 0:
    r *= -1
if r == 0:
    print("Last digit of {} is {} and is 0".format(n, r))
elif r > 5:
    print("Last digit of {} is {} and is greater than 5".format(n, r))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, r))
