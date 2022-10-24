#!/usr/bin/python3
"""create a class raises exception."""


class BaseGeometry:
    """a class raises exception."""
    def area(self):
        """raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates input"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
