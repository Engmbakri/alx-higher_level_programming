#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for i in my_lsit:
            new_list.append(i % 2 == 0)
        return new_list
