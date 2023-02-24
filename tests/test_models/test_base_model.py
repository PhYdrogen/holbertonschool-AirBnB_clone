import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class Testbase(unittest.TestCase):

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
        bmbeforesave = bm.to_dict()
        bm.save()
        self.assertFalse(bm.to_dict() != bmbeforesave)

    def test_str(self):
        md = BaseModel()
        self.assertEqual(type(str(md)), str)


if __name__ == '__main__':
    unittest.main()
