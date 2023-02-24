import unittest
from models.engine.file_storage import FileStorage
import os


class Teststorage(unittest.TestCase):

    @classmethod
    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_filepath(self):
        fs = FileStorage()
        self.assertEqual(type(fs._FileStorage__file_path), str)

    def test_obj(self):
        fs = FileStorage()
        self.assertEqual(type(fs._FileStorage__objects), dict)

    def test_all(self):
        fs = FileStorage()
        self.assertEqual(type(fs.all()), dict)

    def test_new(self):
        from models.base_model import BaseModel
        fs = FileStorage()
        item = BaseModel()
        fs.new(item)
        self.assertTrue(len(fs.all()) > 0)

    def test_save(self):
        from models.base_model import BaseModel
        import datetime
        fs = FileStorage()
        fs.reload()
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
        fs.reload()
        all_obj_as_dict = fs.all()
        for key, obj in all_obj_as_dict.items():
            self.assertEqual(key, "{}.{}".format(obj.__class__.__name__, obj.id))
            self.assertTrue(isinstance(obj, BaseModel))

    def test_reload(self):
        fs = FileStorage()
        fs.reload()
        self.assertTrue(fs.all())

    def test_bmsave(self):
        from models.base_model import BaseModel
        fs = FileStorage()
        item = BaseModel()
        fs.new(item)
        item.save()

        save_storage = fs.all()
        fs.reload()
        self.assertTrue(save_storage == fs.all())

    def test_bminit(self):
        from models.base_model import BaseModel
        md = BaseModel(id="52")

        self.assertEqual(md.id, "52")


if __name__ == '__main__':
    unittest.main()
