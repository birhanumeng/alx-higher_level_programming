#!/usr/bin/python3
"""Define function tha append string to a file."""


def read_lines(filename="", nb_lines=0):
    """prints number of lines in a text file."""
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return

        lines = 0
        for line in f:
            lines += 1
        f.seek(0)
        if nb_lines >= lines:
            print(f.read(), end="")
            return

        else:
            n = 0
            while n < nb_lines:
                print(f.readline(), end="")
                n += 1
