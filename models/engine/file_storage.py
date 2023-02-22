#!/usr/bin/python3
import json
import os
from datetime import datetime

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
        return FileStorage.__objects
        
    def new(self, obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
        
    def save(self):
        obj_to_dict = FileStorage.__objects.copy()
        for key, obj in obj_to_dict.items():
            obj_to_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_to_dict, f)

    def reload(self):
        if not os.path.exists(self.__class__.__file_path):
            with open(self.__class__.__file_path, "w", encoding="utf-8") as f:
                json.dump({}, f)
            
        with open(self.__class__.__file_path, "r", encoding="utf-8") as f:
            self.__class__.__objects = json.load(f)
        f.close()
