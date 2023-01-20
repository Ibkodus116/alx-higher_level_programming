#!/usr/bin/python3
"""Module Doc for a longe thing"""
import json


class Base:
    """Class Base Doc"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert To json string"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        name = cls.__name__
        list_dict = []
        if list_objs:
            for objs in list_objs:
                list_dict += [objs.to_dictionary()]
        else:
            pass

        with open(f"{name}.json", "w") as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        "Return json strings to python Dict obj"
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 4)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new
