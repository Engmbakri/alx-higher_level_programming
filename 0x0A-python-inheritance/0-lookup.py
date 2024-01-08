#!/usr/bin/python3

# function that returns the list of attributes and methods
def lookup(obj):
    attributes_methods = dir(obj)

    # filter any item start with '__'
    filters = [item for item in attributes_methods if not startswith("__")]
    return filters
