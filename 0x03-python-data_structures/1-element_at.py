#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
    """Print list element at a specific index."""
    if idx < 0 or idx >= len(my_list):
        return None
    print("Element at index {:d} is {}".format(idx, my_list[idx]))
