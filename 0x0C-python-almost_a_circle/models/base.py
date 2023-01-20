#!/usr/bin/python3
import json
"""Module Doc for a longe thing"""


class Base:
    """Class Base Doc"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """convert To json string"""
        if not list_dictionaries:
            return list_dictionaries
        return json.dumps(list_dictionaries)
