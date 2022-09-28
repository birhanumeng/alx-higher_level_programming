#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace 'search' with 'replace' in a list."""
    tmp = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] == search:
            tmp[i] = replace
    return (tmp)
