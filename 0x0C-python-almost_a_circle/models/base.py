#!/usr/bin/python3
""" Class Base """
import json
import os


class Base:
    """ Definition of class Base """
    __nb_objects = 0
    def __init__(self, id=None):
        """ init class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json way """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ safe .json """
        sweeps = list()
        tag = cls.__name__ +".json"
        with open(tag, mode="w", encoding="utf-8") as coso:
            if list_objs:
                sweeps = [steps.to_dictionary() for steps in list_objs]
            coso.write(cls.to_json_string(sweeps))

    @staticmethod
    def from_json_string(json_string):
        """ json to list """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)
