""" BASE MODEL CLASS """
import uuid
from datetime import date


class BaseModel:
    
    def __init__(self):
        id = str(uuid.uuid4())
        create_at = date.today()
        update_at = date.today()

    def __str__ (self):
        return f"[{type(self)} ({self.id} {self.__dict__})]"