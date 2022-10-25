#!/usr/bin/python3
"""Define function tha append string to a file."""


def append_write(filename="", text=""):
    """append string to a file."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
