#!/usr/bin/python3
"""Define function to write object file."""


import json


def save_to_json_file(my_obj, filename):
    """Writes oject file to file using JSON representation."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
