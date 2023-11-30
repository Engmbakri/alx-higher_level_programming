#!/usr/bin/python3
def add(a, b):
    return a + b 
def sub(a, b):
    return a -b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
if __name__ == "__main__":
    import calculator_1
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, int(div(a, b))))
