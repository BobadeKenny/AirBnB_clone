#!/usr/bin/python3
"""
This class handles the flow of serialization-deserialization
"""

import json


class FileStorage:
    """
    a class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances
    """
    __file_path = "storage.json"
    __objects = {}
    def all(self):
        """
        Returns:
            dict: the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Returns:
            None
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        Returns:
            None
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """
        deserializes the JSON file to __objects
        Returns:
            None
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                json_dict = json.loads(f.read())
                for k, v in json_dict.items():
                    self.__objects[k] = v
        except IOError:
            pass
