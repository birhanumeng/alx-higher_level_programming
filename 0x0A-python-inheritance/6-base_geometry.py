#!/usr/bin/python3
"""create a class raising exception"""


class BaseGeometry:
    """A class raises exception."""
    def area(self):
        """raises an exception."""
        raise Exception("area() is not implemented")
