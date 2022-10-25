#!/usr/bin/python3
"""Define function to inserts lines to files."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts lines to a file."""
    file_ = ""
    with open(filename) as f:
        for line in f:
            file_ += line
            if search_string in line:
                file_ += new_string
    with open(filename, "w") as f:
        f.write(text)
