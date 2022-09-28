#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    mult = 0
    sum = 0
    for x in my_list:
        mult += x[0] * x[1]
    for x in my_list:
        sum += x[1]
    return mult/sum
