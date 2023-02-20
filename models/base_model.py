""" BASE MODEL CLASS """
import uuid
from datetime import date


class BaseModel:
    
    
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.create_at = date.today()
        self.update_at = date.today()

    def __str__(self):
        return f"[{self.__class__.__name__} ({self.id} {self.__dict__})]"
    
    def save():
        
    
    def to_dict():
        