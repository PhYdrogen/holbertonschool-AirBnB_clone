import unittest
from models.state import State


class Teststate(unittest.TestCase):

    def test_name(self):
        State.name = "Toulouse"
        self.assertEqual(State.name, "Toulouse")


if __name__ == '__main__':
    unittest.main()
