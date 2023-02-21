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
        #for k, o in obj.items():
        #        if (not isinstance(o, str)):
        #            obj[k] = str(obj[k])    
        self.__class__.__objects["{}.{}".format(obj["__class__"], obj["id"])] = obj
        
    def save(self):
        with open(self.__class__.__file_path, "w", encoding="utf-8") as f:
            #print(self.__class__.__objects)
            #for l,k in self.__class__.__objects.items():
            #    print("{} {}".format(k.get(id, "PAS D ID"), l))

            json.dump(self.__class__.__objects, f)

    def reload(self):
        if not os.path.exists(self.__class__.__file_path):
            return
        with open(self.__class__.__file_path, "r", encoding="utf-8") as f:
            self.__class__.__objects = json.load(f)