#!/usr/bin/python3

"""
Save to from python to json in a file
"""
import json


def load_from_json_file(filename):
    """Save json into in a file"""
    with open(filename) as f:
        return json.load(f)
