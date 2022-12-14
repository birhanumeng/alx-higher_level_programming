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
        size (int): size for __size
        """
        self.__size = size

    def area(self):
        """Calculates area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Gets the size of the object"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the object"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
