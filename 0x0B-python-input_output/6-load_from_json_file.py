#!/usr/bin/python3
"""Define function that create object from JSOn."""
import json


def load_from_json_file(filename):
    """Create object from JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return(json.load(f))
