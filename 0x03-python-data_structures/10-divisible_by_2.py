#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    else:
        result = []
        for i in my_lsit:
            result.append(i % 2 == 0)
        return result
