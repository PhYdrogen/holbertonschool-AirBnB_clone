""" BASE MODEL CLASS """
import uuid
from datetime import datetime

class BaseModel:
    """" Class basemodel """
    
    
    def __init__(self, *args, **kwargs):
        """ init """
        self.id = str(uuid.uuid4())
        self.created_at = self.getDate()
        self.update_at = self.getDate()

    def __str__(self):
        return f"[{self.__class__.__name__} ({self.id} {self.__dict__})]"
    
    def save(self):
        self.update_at = self.getDate()
    
    def to_dict(self):
        return self.__dict__
        #new_dict["__class__"] = self.__class__.__name__
        #return new_dict
    
    @staticmethod
    def getDate():
        return datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")