import unittest
from models.amenity import Amenity


class Testamentiy(unittest.TestCase):

    def test_name(self):
        self.assertEqual(type(Amenity.name), str)


if __name__ == '__main__':
    unittest.main()
