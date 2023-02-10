import unittest
import random
from src.main.python import hangman


class HangmanTests(unittest.TestCase):
    #test case for displaying hangman
    def test_display_hangman(self):
        tries = 4
        result = hangman.display_hangman(tries)
        self.assertEqual( """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """, result)
    def test_word_bank(self):
        self.assertIn(hangman.pick_word("easy"),hangman.easy_wordbank)

    def test_play_game(self):
        random.seed(0)
        result = hangman.play_game()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()