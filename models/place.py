#!/usr/bin/python3
from models.base_model import BaseModel

class Place(BaseModel):
    
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitdue = 0.0
    longitude = 0.0
    amenity_ids = []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.city_id = kwargs.get("state_id",  "")
        self.user_id = kwargs.get("user_id",  "")
        self.name = kwargs.get("name",  "")
        self.description = kwargs.get("description",  "")
        self.number_rooms = kwargs.get("number_rooms",  0)
        self.number_bathrooms = kwargs.get("number_bathrooms",  0)
        self.max_guest = kwargs.get("max_guest",  0)
        self.price_by_night = kwargs.get("price_by_night",  0)
        self.latitdue = kwargs.get("latitdue",  0.0)
        self.longitude = kwargs.get("longitude",  0.0)
        self.amenity_ids = kwargs.get("amenity_ids",  [])
