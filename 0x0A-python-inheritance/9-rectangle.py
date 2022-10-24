#!/usr/bin/python3
"""creat a class inherits from BaseGeometry class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry class"""
    def __init__(self, width, height):
        """initializes an instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area"""
        return self.__width * self.__height

    def __str__(self):
        """for representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
