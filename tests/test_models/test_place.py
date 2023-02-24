import unittest
from models.place import Place


class Testplace(unittest.TestCase):

    def test_cid(self):
        self.assertEqual(type(Place.city_id), str)

    def test_uid(self):
        self.assertEqual(type(Place.user_id), str)

    def test_name(self):
        self.assertEqual(type(Place.name), str)

    def test_desc(self):
        self.assertEqual(type(Place.description), str)

    def test_nr(self):
        self.assertEqual(type(Place.number_rooms), int)

    def test_nb(self):
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_mg(self):
        self.assertEqual(type(Place.max_guest), int)

    def test_pbn(self):
        self.assertEqual(type(Place.max_guest), int)

    def test_la(self):
        self.assertEqual(type(Place.latitude), float)

    def test_lo(self):
        self.assertEqual(type(Place.longitude), float)

    def test_amids(self):
        self.assertEqual(type(Place.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
