#!/usr/bin/python3
from models.base_model import BaseModel

class Amenity(BaseModel):
    
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.place_id = ""
        self.user_id = ""
        self.text = ""
