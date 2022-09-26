#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for num in my_list[1:]:
            if num > max:
                max = num
        return max
