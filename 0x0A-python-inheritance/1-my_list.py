#!/usr/bin/python3
"""Define a class MyList inherited list class."""


class MyList(list):
    """Implements sorted methods for the list class."""

    def print_sorted(self):
        """Print a list in sorted and ascending order."""
        print(sorted(self))
