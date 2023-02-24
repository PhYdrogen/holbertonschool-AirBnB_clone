import unittest
from models.review import Review


class Testreview(unittest.TestCase):

    def test_pid(self):
        Review.place_id = "001"
        self.assertEqual(Review.place_id, "001")

    def test_uid(self):
        Review.user_id = "002"
        self.assertEqual(Review.user_id, "002")

    def test_txt(self):
        Review.text = "002"
        self.assertEqual(Review.text, "002")


if __name__ == '__main__':
    unittest.main()
