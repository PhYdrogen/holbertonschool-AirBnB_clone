import unittest
from models.state import State


class Teststate(unittest.TestCase):

    def test_name(self):
        self.assertEqual(type(State.name), str)


if __name__ == '__main__':
    unittest.main()
