#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """find multiple of 2 in the list."""
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
