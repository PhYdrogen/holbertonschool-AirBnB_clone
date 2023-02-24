import unittest
from models.user import User


class Testbase(unittest.TestCase):

    def test_mail(self):
        User.email = "red@gmail.com"
        self.assertEqual(User.email, "red@gmail.com")

    def test_pwd(self):
        User.password = "unit3stf0rlif3"
        self.assertEqual(User.password, "unit3stf0rlif3")

    def test_fn(self):
        User.first_name = "Gab"
        self.assertEqual(User.first_name, "Gab")

    def test_ln(self):
        User.last_name = "God"
        self.assertEqual(User.last_name, "God")


if __name__ == '__main__':
    unittest.main()
