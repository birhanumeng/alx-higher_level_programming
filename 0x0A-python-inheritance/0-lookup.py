#!/usr/bin/python3
"""Defines a lookup function for object's attributes."""


def lookup(obj):
    """Return a list of an object's attributes."""
    return (dir(obj))
