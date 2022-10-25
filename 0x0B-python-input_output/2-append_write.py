#!/usr/bin/python3
"""Define function tha append string to a file."""


def read_lines(filename="", nb_lines=0):
    """prints number of lines in a text file."""
    with open(filename, encoding='utf-8') as file:
        if nb_lines <= 0:
            for line in file:
                print(line, end="")
        else:
            for line in range(nb_lines):
                print(file.readline(), end="")
