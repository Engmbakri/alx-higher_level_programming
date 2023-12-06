#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {k: 2 * v for v,k in a_dictionary.items()}
