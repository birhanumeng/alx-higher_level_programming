#!/usr/bin/python3
"""Define class for students"""


class Student(object):
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initializing"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieving"""
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dictionary[key] = value
        return dictionary

    def reload_from_json(self, json):
        """replace arguments"""
        for key, value in json.items():
            setattr(self, key, value)
