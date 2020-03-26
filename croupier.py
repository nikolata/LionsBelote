import random
from belote_constants import BELOTE_ALL_CARDS, BELOTE_ALL_TYPES_OF_GAME
def shuffle_list_of_cards():
	shuffled_deck = BELOTE_ALL_CARDS
	random.shuffle(shuffled_deck)
	return shuffled_deck
def set_type_of_game():
	type_of_game = BELOTE_ALL_TYPES_OF_GAME
	return random.choice(type_of_game)