#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = sorted(a_dictionary.keys())
    for k in k:
        print("{}: {}".format(k, a_dictionary[k]))
