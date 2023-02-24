import unittest
from models.city import City


class Testbase(unittest.TestCase):

    def test_name(self):
        self.assertEqual(type(City.name), str)

    def test_sid(self):
        self.assertEqual(type(City.state_id), str)


if __name__ == '__main__':
    unittest.main()
