#!/usr/bin/python3
''' module for is_same _class method'''


def is_same_class(obj, a_class):
    ''' function checks if the objects is
    exactly inistance of specific class'''

    return type(obj) is a_class
