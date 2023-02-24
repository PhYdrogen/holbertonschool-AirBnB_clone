import unittest
from models import storage
import os


class Teststorage(unittest.TestCase):

    @classmethod
    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_filepath(self):
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_obj(self):
        self.assertEqual(type(storage._FileStorage__objects), dict)

    def test_all(self):
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        from models.base_model import BaseModel
        item = BaseModel()
        storage.new(item)
        self.assertTrue(len(storage.all()) > 0)

    def test_save(self):
        from models.base_model import BaseModel
        import datetime
        storage.reload()
        if os.path.exists("file.json"): # si il existe sort une erreur
            self.assertTrue(False)

        bm = BaseModel()
        before = bm.updated_at
        bm.save()
        if not os.path.exists("file.json"): # si il existe PAS sort une erreur
            self.assertTrue(False)
        self.assertTrue(before == bm.updated_at)
        self.assertEqual(type(before), datetime.datetime)
        self.assertEqual(type(bm.updated_at), datetime.datetime)
        storage.reload()
        all_obj_as_dict = storage.all()
        for key, obj in all_obj_as_dict.items():
            self.assertEqual(key, "{}.{}".format(obj.__class__.__name__, obj.id))
            self.assertTrue(isinstance(obj, BaseModel))        

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

class Teststorage_reload(unittest.TestCase):

    @classmethod
    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_reload(self):
        from models.base_model import BaseModel
        storage.all().clear()

        bm = BaseModel()
        storage.save()
        # écris dans le hdd
        storage.all().clear()
        # vide le dict
        storage.reload()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertTrue(isinstance(obj, BaseModel))


if __name__ == '__main__':
    unittest.main()
