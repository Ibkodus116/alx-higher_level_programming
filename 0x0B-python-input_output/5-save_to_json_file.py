#!/usr/bin/python3

"""
Save to from json to python in a file
"""
import json


def save_to_json_file(my_obj, filename):
    """Save json dumos in a file"""
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
