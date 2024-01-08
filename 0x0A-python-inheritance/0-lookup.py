#!/usr/bin/python3
''' Method for lookup method'''


def lookup(obj):
    '''function that returns the list of attributes and methods
    Argus:
    obj (object) : object to list

    Returns:
    list: the list of attibutes
    '''
    return dir(obj)
