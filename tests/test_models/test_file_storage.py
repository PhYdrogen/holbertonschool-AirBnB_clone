import unittest
from models import storage
from datetime import datetime
import os

class Testsorage(unittest.TestCase):
    
    def test_filepath(self):
        self.assertTrue(storage.__file_path)
    
    def test_obj(self):
        self.assertTrue(storage.__objects)
        
    def test_all(self):
        self.assertEqual(type(storage.all()), dict)
        
    def test_new(self):
        from models.base_model import BaseModel
        item = BaseModel()
        save_storage = storage.all()
        storage.new(item)
        self.assertFalse(save_storage == storage.all())

    def test_save(self):
        from models.base_model import BaseModel
        item = BaseModel()
        storage.new(item)
        storage.save()
        
        save_storage = storage.all()
        storage.reload()
        self.assertTrue(save_storage == storage.all())
    
    def test_reload(self):
        storage.reload()
        self.assertTrue(os.path.exists(self.__class__.__file_path))
        
    def test_bmsave(self):
        from models.base_model import BaseModel
        item = BaseModel()
        storage.new(item)
        item.save()
        
        save_storage = storage.all()
        storage.reload()
        self.assertTrue(save_storage == storage.all())
        
    def test_bminit(self):
        from models.base_model import BaseModel
        md = BaseModel(id="52")
      
        self.assertEqual(md.id, "52")



if __name__ == '__main__':
    unittest.main()
 