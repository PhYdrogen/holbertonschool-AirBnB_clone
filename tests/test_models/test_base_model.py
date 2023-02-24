import os
import unittest
from models.base_model import BaseModel
from datetime import datetime


class Testbase(unittest.TestCase):

    @classmethod
    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_id(self):
        md = BaseModel()
        self.assertEqual(type(md.id), str)

    def test_updateat(self):
        md = BaseModel()
        last_type = type(md.updated_at)
        d_json = md.to_dict()
        new_type = type(d_json['updated_at'])
        self.assertFalse(last_type == new_type)

    def test_updateat(self):
        md = BaseModel()
        self.assertTrue(isinstance(md.created_at, datetime))

    def test_save(self):
        bm = BaseModel()
        before = bm.updated_at
        bm.save()
        self.assertTrue(before == bm.updated_at)

    def test_str(self):
        bm = BaseModel()
        self.assertTrue(str(bm))
        self.assertEqual(str(bm), "[{}] ({}) {}".format(bm.__class__.__name__, bm.id, bm.__dict__))

    def test_to_dict(self):
        bm = BaseModel()
        bm.updated_at = datetime.utcnow()
        d_json = bm.to_dict()
        self.assertEqual(type(d_json), dict)
        self.assertEqual(type(d_json['id']), str)
        self.assertEqual(type(d_json['created_at']), str)
        self.assertEqual(type(d_json['__class__']), str)
        self.assertEqual(d_json['__class__'], "BaseModel")

if __name__ == '__main__':
    unittest.main()
