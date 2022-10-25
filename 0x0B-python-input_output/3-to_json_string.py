#!/usr/bin/python3
"""Define function to convert to JSON."""


import json


def to_json_string(my_obj):
    """convert to JSON representation."""
    return json.dumps(my_obj)
