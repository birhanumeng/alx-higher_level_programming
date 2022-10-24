#!/usr/bin/python3
"""define module to check inheritance object"""


def inherits_from(obj, a_class):
    """returns True or False."""
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
