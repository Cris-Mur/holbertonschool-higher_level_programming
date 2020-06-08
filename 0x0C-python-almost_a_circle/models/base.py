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
        sheeps = list()
        tag = cls.__name__ +".json"
        with open(tag, mode="w", encoding="utf-8") as coso:
            if list_objs:
                sheeps = [steps.to_dictionary() for steps in list_objs]
            coso.write(cls.to_json_string(sheeps))

    @staticmethod
    def from_json_string(json_string):
        """ json to list """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ set instanses from dict """
        if cls.__name__ == "Rectangle":
            coso = cls(1, 1)
        if cls.__name__ == "Square":
            coso = cls(1)
        coso.update(**dictionary)
        return coso

    @classmethod
    def load_from_file(cls):
        """ read file """
        namae = "{}.json".format(cls.__name__)
        if not os.path.isfile(namae):
            return []
        with open(namae, mode="r", encoding="utf-8") as bear:
            return [cls.create(**coso)
                    for coso in cls.from_json_string(bear.read())]
