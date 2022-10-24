#!/usr/bin/python3
"""create a class inherits from Rectangle class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle class."""
    def __init__(self, size):
        """Initializes an instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """for informal string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
