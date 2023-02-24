import unittest
from models.place import Place


class Testplace(unittest.TestCase):

    def test_cid(self):
        Place.city_id = "001"
        self.assertEqual(Place.city_id, "001")

    def test_uid(self):
        Place.user_id = "002"
        self.assertEqual(Place.user_id, "002")

    def test_name(self):
        Place.name = "Red"
        self.assertEqual(Place.name, "Red")

    def test_desc(self):
        Place.description = "Good name bro"
        self.assertEqual(Place.description, "Good name bro")

    def test_nr(self):
        Place.number_rooms = 4
        self.assertEqual(Place.number_rooms, 4)

    def test_nb(self):
        Place.number_bathrooms = 1
        self.assertEqual(Place.number_bathrooms, 1)

    def test_mg(self):
        Place.max_guest = 55
        self.assertEqual(Place.max_guest, 55)

    def test_pbn(self):
        Place.price_by_night = 2000
        self.assertEqual(Place.price_by_night, 2000)

    def test_la(self):
        Place.latitude = 1.2
        self.assertEqual(Place.latitude, 1.2)

    def test_lo(self):
        Place.longitude = 2.5
        self.assertEqual(Place.longitude, 2.5)

    def test_amids(self):
        self.assertEqual(type(Place.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
