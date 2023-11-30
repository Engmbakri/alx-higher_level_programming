#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    arguments = argv[1:]
    if len (arguments) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    result = 0
    if op == "+":
        print(add(a, b))
    elif op == "-":
        print(sub(a, b))
    elif op == "*":
        print(mul(a, b))
    elif op == "/":
        print(div(a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
