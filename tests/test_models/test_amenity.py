import unittest
from models.amenity import Amenity

class Testamentiy(unittest.TestCase):
    
    def test_name(self):
        Amenity.name = "Toulouse"
        self.assertEqual(Amenity.name, "Toulouse")
    
    def test_uid(self):
        Amenity.user_id = "0008"
        self.assertEqual(Amenity.user_id, "0008")
    
    def test_txt(self):
        Amenity.text = "Hello World"
        self.assertEqual(Amenity.text, "Hello World")

if __name__ == '__main__':
    unittest.main()
 