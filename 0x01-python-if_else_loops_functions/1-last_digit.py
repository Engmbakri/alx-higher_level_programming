#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last *= -1
print("Last digit of", end=" ")
if last > 5:
    print("{:d} is {:d} and is greater than 5".format(number, last))
elif last == 0:
    print("{:d} is {:d} and is 0".format(number, last))
elif last < 6 and last != 0:
    print("{:d} is {:d} and is less than 6 and not 0".format(number, last))
