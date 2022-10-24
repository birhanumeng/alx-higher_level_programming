#!/usr/bin/python3
"""create a class inherits from list class."""


class MyList(list):
    """Implements sorted printing."""

    def print_sorted(self):
        """Print a list in sorted and ascending order."""
        print(sorted(self))
