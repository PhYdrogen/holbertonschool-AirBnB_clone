import uuid
from datetime import datetime
from models import storage
date_now = datetime.now()


class BaseModel:
    """ Classe base model """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                if key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
        else:
            self.id = str(uuid.uuid4())

            self.created_at = date_now
            self.updated_at = date_now
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        storage.save()
        self.updated_at = date_now

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
