#!/usr/bin/python3
"""Defines function for inserting string"""


def write_file(filename="", text=""):
    """Write a string to text file using UTF8 encoding."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
