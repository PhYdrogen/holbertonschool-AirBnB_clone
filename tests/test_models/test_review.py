import unittest
from models.review import Review

class Testreview(unittest.TestCase):
    
    def test_pid(self):
        self.assertEqual(type(Review.place_id), str)
        
    def test_uid(self):
        self.assertEqual(type(Review.user_id), str)
    
    def test_txt(self):
        self.assertEqual(type(Review.text), str)

if __name__ == '__main__':
    unittest.main()
 