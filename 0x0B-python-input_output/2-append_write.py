#!/usr/bin/python3
"""Define function tha append string to a file."""


def read_lines(filename="", nb_lines=0):
    """prints number of lines in a text file."""
    line_count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for line in f:
            if line_count < nb_lines:
                print(line, end="")
                line_count += 1
