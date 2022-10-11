#!/usr/bin/python3
"""Square class"""


class Square:
    """A class named Square
    Attributes:
    attr1 (size): size of square
    """
    def __init__(self, size=0):
        """
        Args:
        size (int): size for __size attribute
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates area"""
        return self.__size * self.__size
