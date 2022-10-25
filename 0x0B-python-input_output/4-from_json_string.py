#!/usr/bin/python3
"""Define function covert JSON to python string object."""
import json


def from_json_string(my_str):
    """Convert from JSON representation to python object."""
    return(json.loads(my_str))
