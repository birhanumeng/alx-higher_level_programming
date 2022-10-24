#!/usr/bin/python3
"""create a class inherits from int class."""


class MyInt(int):
    """Inherits from int class"""

    def __eq__(self, other):
        """Swaps builtin"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """define swaps"""
        return int.__eq__(self, other)
