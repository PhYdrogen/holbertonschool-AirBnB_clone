#!/usr/bin/python3
import json
import os

class FileStorage:
    """ FileStorage
    __init__
    all
    new
    save
    reload
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__class__.__objects
        
    def new(self, obj):
        obj = obj.to_dict()
        self.__class__.__objects["{}.{}".format(obj["__class__"], obj["id"])] = obj
        
    def save(self):
        with open(self.__class__.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__class__.__objects, f)
        f.close()

    def reload(self):
        if not os.path.exists(self.__class__.__file_path):
            return
        with open(self.__class__.__file_path, "r", encoding="utf-8") as f:
            self.__class__.__objects = json.load(f)
        f.close()