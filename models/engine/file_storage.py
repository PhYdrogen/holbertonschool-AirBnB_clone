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
    def __init__(self, file = "", obj = {}):
        self.__file_path = file
        self.__objects = obj
        
    def all(self):
        return self.__objects
        
    def new(self, obj):
        self.__objects = obj
        
    def save(self):
        with open(self.__file_path, "a", encoding="utf-8") as f: 
            self.__objects = json.dump(self.__objects, f)

    def reload(self):
        if not os.path.exists(self.__file_path):
            
            return
        with open(self.__file_path, "r", encoding="utf-8") as f: 
            self.__objects = json.load(f)