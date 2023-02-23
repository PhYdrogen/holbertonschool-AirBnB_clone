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
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State

        if not os.path.exists(self.__class__.__file_path):
            return
            
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            big_dict = json.load(f)
            for baseid, value in big_dict.items():
                classe = value["__class__"]
                obj = eval(classe)(**value)
                self.new(obj)
