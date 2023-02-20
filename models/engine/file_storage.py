#!/usr/bin/python3
import json


class FileStorage:
    """ FileStorage
    __init__
    all
    new
    save
    reload
    """
    def __init__(self, file = None, obj = None):
        self.__file_path = file
        self.__objects = obj
        
    def all(self):
        return self.__objects
        
    def new(self, obj):
        self.__object = obj
        
    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as f: 
            self.__object = json.dump(self.__object, f)
        
    def reload(self):
        with open(self.__file_path, "r", encoding="utf-8") as f: 
            self.__object = json.load(f)
