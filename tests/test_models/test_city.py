import unittest
from models.city import City

class Testbase(unittest.TestCase):
    
    def test_name(self):
        City.name = "Toulouse"
        self.assertEqual(City.name, "Toulouse")
    
    def test_sid(self):
        City.state_id = "0001"
        self.assertEqual(City.state_id, "0001")

if __name__ == '__main__':
    unittest.main()
 