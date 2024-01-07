#!/usr/bin/python3
"module to add two integers"


def add_integer(a, b=98):
    """
    fucton adds two integers


    parameters:
    a (int or float): The first number
    b (int or float): The second number

    Raises:
    TypeError: if a or b not is not integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)

    result = a + b
    return result


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
