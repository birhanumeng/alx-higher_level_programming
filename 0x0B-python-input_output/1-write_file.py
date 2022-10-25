#!/usr/bin/python3
"""Define a function for read a string."""


def number_of_lines(filename=""):
    """Returns number of lines in a text file."""
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            count += 1
        return count
