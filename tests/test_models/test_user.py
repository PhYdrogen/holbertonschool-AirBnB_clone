import unittest
from models.user import User

class Testbase(unittest.TestCase):
    
    def test_mail(self):
        self.assertEqual(type(User.email), str)
    
    def test_pwd(self):
        self.assertEqual(type(User.password), str)
        
    def test_fn(self):
        self.assertEqual(type(User.first_name), str)
    
    def test_ln(self):
        self.assertEqual(type(User.last_name), str)



if __name__ == '__main__':
    unittest.main()
 