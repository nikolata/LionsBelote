import unittest
from croupier import (
    shuffle_list_of_cards,
    set_type_of_game,
    Card
)
from belote_constants import BELOTE_ALL_CARDS


class TestShuffle(unittest.TestCase):
    def test_if_return_shuffled_list_of_cards(self):
        deck = BELOTE_ALL_CARDS
        result = shuffle_list_of_cards()

        for card in result:
            self.assertIsInstance(card, Card)

        
    def test_if_return_shuffled_list_with_same_len(self):
        deck = BELOTE_ALL_CARDS
        result = shuffle_list_of_cards()

        self.assertEqual(len(result),len(deck))

class TestSetTypeOfGame(unittest.TestCase):
    def test_if_return_one_color(self):
        color = set_type_of_game()
        self.assertTrue(isinstance(color,str))


if __name__ == '__main__':
    unittest.main()
