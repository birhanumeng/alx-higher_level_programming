#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Print key and value in a dictionary ordered by key."""
    for key in a_dictionary.item():
        print("{}: {}".format(key, a_dictionary[key]))
