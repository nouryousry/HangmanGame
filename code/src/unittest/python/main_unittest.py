import unittest
import random
from src.main.python import main

class MyTestCase(unittest.TestCase):
    def test_play_game(self):
        random.seed(0)
        result = main.play_game()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
