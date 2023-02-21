""" BASE MODEL CLASS """
import uuid
from datetime import datetime
from models import storage
formatage = "%Y-%m-%dT%H:%M:%S.%f"
class BaseModel:
    """" Class basemodel """
 
    
    
    def __init__(self, *args, **kwargs):
        """ init """
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "created_at":
                    self.created_at = datetime.strptime(value, formatage)
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value, formatage)

        else:
            self.id = self.getID()
            self.created_at = self.getDate()
            self.updated_at = self.getDate()
            storage.new(self)


    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__})]"
    
    def save(self):
        """ fait une sauvegarde de l'instance et actualise updated_at en datetime.datetime """
        storage.new(self)
        storage.save()
        self.updated_at = f"{self.getDate()}"
    
    def to_dict(self):
        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at
        new_dict["updated_at"] = self.updated_at
        return new_dict
    
    @staticmethod
    def getDate():
        """ retourne la date en datetime.datetime """
        return datetime.now()
        
    @staticmethod
    def getID():
        return str(uuid.uuid4())