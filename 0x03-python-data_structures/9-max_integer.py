#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        copy_list = my_list.copy()
        copy_list.sort()
        max_value = copy_list[-1]
        print("Max: {:d}".format(max_value))
