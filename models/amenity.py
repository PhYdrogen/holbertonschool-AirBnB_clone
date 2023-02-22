#!/usr/bin/python3
from models.base_model import BaseModel

class Amenity(BaseModel):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.name = kwargs.get("name",  "")
        self.user_id = kwargs.get("user_id",  "")
        self.text = kwargs.get("text",  "")
