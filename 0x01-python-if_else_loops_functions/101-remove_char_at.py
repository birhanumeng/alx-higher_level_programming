#!/usr/bin/python3
def remove_char_at(str, n):
    tmp = ""
    if n >= 0:
        tmp += str[:n]
        tmp += str[n+1:]
    else:
        tmp = str
    return tmp
