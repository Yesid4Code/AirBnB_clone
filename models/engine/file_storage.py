#!/usr/bin/python3
""" file_storage module that recreate the BaseModel class. """
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Class that:
        - serializes instances to a JSON file.
        - deserializes JSON file to instances.
    """
    __file_path = file.json
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """ Return the dictionary '__objects'. """
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with
            key: <obj class name>.id
        """
        FileStorage.__objects["{}.{}".
                              format(obj.__.class__.__name__, obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file. """
        dic = {}
        for key, value in FileStorage.__objects.items():
            dic.update({key: value.to_dic()})

        with open(FileStorage.__file_path, "w") as fil:
            json.dump(dic, file)
