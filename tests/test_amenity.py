import unittest
from models.amenity import Amenity


class Testamentiy(unittest.TestCase):

    def test_name(self):
        Amenity.name = "Toulouse"
        self.assertEqual(type(Amenity.name), str)

    def test_uid(self):
        Amenity.user_id = "0008"
        self.assertEqual(type(Amenity.user_id), str)

    def test_txt(self):
        Amenity.text = "Hello World"
        self.assertEqual(type(Amenity.text), str)


if __name__ == '__main__':
    unittest.main()
