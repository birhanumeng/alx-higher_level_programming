#!/usr/bin/python3
"""Defines function reads text file."""


def read_file(filename=""):
    """Print text file in UTF8 encoding."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
