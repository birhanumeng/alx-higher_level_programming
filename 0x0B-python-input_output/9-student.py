#!/usr/bin/python3
"""Define class for students."""


class Student(object):
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initializing"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves"""
        return self.__dict__
