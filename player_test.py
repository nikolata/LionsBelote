import unittest
from belote_constants import *
from player import Player
from card import Card


class TestPlayer(unittest.TestCase):
	#
	def test_with_given_non_string_should_raise_TypeError(self):
		name = 123

		with self.assertRaises(AssertionError):
			player = Player(name=name)
	def test_with_given_string_should_create_instance(self):
		name = 'Gosho'

		player = Player(name= name)

		self.assertIsNotNone(player)
		self.assertEqual(name,player.name)
		self.assertEqual([],player.cards)
		self.assertEqual({},player.announcements)

	def test_set_cards_with_given_cards_should_set_them(self):
		player = Player(name='Player')
		cards = [Card('7', 's'), Card('8', 's'), Card('9', 's'), Card('10', 'c'), Card('J', 'd'), Card('Q', 'd'), Card('K','h'), Card('A', 's')]

		player.set_cards(cards)

		self.assertEqual(cards, player.cards)

	def test_sort_cards_should_sort_cards(self):
		player = Player(name='Player')
		cards = [Card('8','s'), Card('7', 's') , Card('A', 's'), Card('9', 's'), Card('A' ,'d'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
		player.set_cards(cards)

		player.sort_cards()
		expected = [Card('7', 's'), Card('8' ,'s'), Card('9', 's'), Card('A', 's'), Card('Q', 'd'), Card('A', 'd'), Card('K', 'h'), Card('10', 'c')]

		self.assertEqual(expected, player.cards)


	#get_belotes
	def test_get_belotes_with_0_belotes_in_hand_should_return_empty_list(self):
		player = Player(name='Player')
		cards = [Card('8','s'), Card('7', 's') , Card('A', 's'), Card('9', 's'), Card('J' ,'d'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
		player.set_cards(cards)

		player.sort_cards()
		result = player.get_belotes()
		expected = []

		self.assertEqual(expected, result)

	def test_get_belotes_with_1_belotes_in_hand_should_return_list_of_one_element_queen_color(self):
		player = Player(name='Player')
		cards = [Card('8','s'), Card('7', 's') , Card('A', 's'), Card('K', 'd'), Card('J' ,'d'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
		player.set_cards(cards)

		player.sort_cards()
		result = player.get_belotes()
		expected = ['d']

		self.assertEqual(expected, result)

	def test_get_belotes_with_2_belotes_in_hand_should_return_list_of_two_elements_queens_colors(self):
		player = Player(name='Player')
		cards = [Card('8','s'), Card('7', 's') , Card('Q', 'h'), Card('K', 'd'), Card('J' ,'d'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
		player.set_cards(cards)

		player.sort_cards()
		result = player.get_belotes()
		expected = ['d' , 'h']

		self.assertEqual(expected, result)

	def test_get_belotes_with_3_belotes_in_hand_should_return_list_of_three_elements_queens_colors(self):
		player = Player(name='Player')
		cards = [Card('K','s'), Card('7', 's') , Card('Q', 'h'), Card('K', 'd'), Card('Q' ,'s'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
		player.set_cards(cards)

		player.sort_cards()
		result = player.get_belotes()
		expected = ['s', 'd', 'h']

		self.assertEqual(expected, result)

	def test_get_belotes_with_4_belotes_in_hand_should_return_list_of_four_elements_queens_colors(self):
		player = Player(name='Player')
		cards = [Card('K','s'), Card('Q', 'c') , Card('Q', 'h'), Card('K', 'd'), Card('Q' ,'s'), Card('Q', 'd'), Card('K', 'c'), Card('K', 'h')]
		player.set_cards(cards)

		player.sort_cards()
		result = player.get_belotes()
		expected = ['s', 'd', 'h', 'c']

		self.assertEqual(expected, result)

	#arrange_hand_by_color
	def test_with_given_cards_from_one_color_should_return_list_of_one_element(self):
		player = Player(name='Player')
		cards = [Card('7','s'), Card('8', 's') , Card('9', 's'), Card('10', 's'), Card('J' ,'s'), Card('Q', 's'), Card('K', 's'), Card('A', 's')]
		player.set_cards(cards)
		player.sort_cards()

		result = player.arrange_hand_by_color()
		expected = [cards]

		self.assertEqual(expected, result)

	def test_with_given_cards_from_two_colors_should_return_list_of_two_elements_sorted_by_color(self):
		player = Player(name='Player')
		cards = [Card('J','d'), Card('8', 's') , Card('9', 's'), Card('10', 's'), Card('J' ,'s'), Card('Q', 's'), Card('K', 's'), Card('A', 's')]
		player.set_cards(cards)
		player.sort_cards()

		result = player.arrange_hand_by_color()
		expected = [[Card('8', 's') , Card('9', 's'), Card('10', 's'), Card('J' ,'s'), Card('Q', 's'), Card('K', 's'), Card('A', 's')], [Card('J','d')]]

		self.assertEqual(expected, result)

	def test_with_given_cards_from_three_colors_should_return_list_of_three_elements_sorted_by_color(self):
		player = Player(name='Player')
		cards = [Card('J','d'), Card('8', 's') , Card('9', 's'), Card('10', 'c'), Card('J' ,'s'), Card('Q', 'c'), Card('K', 's'), Card('A', 's')]
		player.set_cards(cards)
		player.sort_cards()

		result = player.arrange_hand_by_color()
		expected = [[Card('8', 's') , Card('9', 's'), Card('J' ,'s'), Card('K', 's'), Card('A', 's')], [Card('J','d')], [Card('10', 'c'), Card('Q', 'c')]]

		self.assertEqual(expected, result)

	def test_with_given_cards_from_four_colors_should_return_list_of_four_elements_sorted_by_color(self):
		player = Player(name='Player')
		cards = [Card('J','d'), Card('8', 'h') , Card('9', 'h'), Card('10', 'c'), Card('J' ,'s'), Card('Q', 'c'), Card('K', 's'), Card('A', 's')]
		player.set_cards(cards)
		player.sort_cards()

		result = player.arrange_hand_by_color()
		expected = [[Card('J' ,'s'), Card('K', 's'), Card('A', 's')], [Card('J','d')], [Card('8', 'h') , Card('9', 'h')], [Card('10', 'c'), Card('Q', 'c')]]

		self.assertEqual(expected, result)

	#set_belotes_in_announcements
	def test_with_given_hand_should_set_belotes_in_announcements(self):
		player = Player(name='Player')
		cards = [Card('K','s'), Card('7', 's') , Card('Q', 'h'), Card('K', 'd'), Card('Q' ,'s'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
		player.set_cards(cards)
		player.sort_cards()
		
		player.set_belotes_in_announcements()

		expected = ['s', 'd', 'h']

		self.assertEqual(expected, player.announcements[BELOTE_BELOTE_STRING])

	# #set_given_sequence
	# def test_with_given_tierce_should_set_correctly(self):
	# 	player = Player(name='Player')
	# 	cards = [Card('K','s'), Card('7', 's') , Card('Q', 's'), Card('J', 's'), Card('9' ,'s'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
	# 	player.set_cards(cards)
	# 	player.sort_cards()

	# 	player.set__in_announcements()

	# 	expected = {BELOTE_TIERCE_STRING : [Card('K', 's')]}

	# 	self.assertEqual(expected, player.announcements)


	#set_sequences_in_announcements
	def test_with_given_tierce_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('K','s'), Card('7', 's') , Card('Q', 's'), Card('J', 's'), Card('9' ,'s'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
		player.set_cards(cards)
		player.sort_cards()

		player.set_sequences_in_announcements()

		expected = {BELOTE_TIERCE_STRING : [Card('K', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_2_tierce_of_one_color_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('A','s'), Card('7', 's') , Card('Q', 's'), Card('K', 's'), Card('9' ,'s'), Card('Q', 'd'), Card('8', 's'), Card('K', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_sequences_in_announcements()

		expected = {BELOTE_TIERCE_STRING : [Card('9', 's'), Card('A', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_2_tierce_of_different_colors_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('A','s'), Card('A', 'h') , Card('Q', 's'), Card('K', 's'), Card('Q' ,'h'), Card('Q', 'd'), Card('K', 'h'), Card('10', 'c')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_sequences_in_announcements()

		expected = {BELOTE_TIERCE_STRING : [Card('A', 's'), Card('A', 'h')]}

		self.assertEqual(expected, player.announcements)


	def test_with_given_quarte_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('7','h'), Card('8', 'c') , Card('7', 's'), Card('Q', 'h'), Card('A' ,'h'), Card('K', 'h'), Card('9', 'h'), Card('J', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_sequences_in_announcements()

		expected = {BELOTE_QUARTE_STRING : [Card('A', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_tierce_and_quarte_of_one_color_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('7','h'), Card('8', 'h') , Card('7', 's'), Card('Q', 'h'), Card('A' ,'h'), Card('K', 'h'), Card('9', 'h'), Card('J', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_sequences_in_announcements()

		expected = {BELOTE_TIERCE_STRING : [Card('9', 'h')],
					BELOTE_QUARTE_STRING : [Card('A', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_tierce_and_quarte_of_different_colors_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('10', 'h'), Card('J', 'c'), Card('7', 'h'), Card('9', 'd'), Card('10', 'c'), Card('Q', 'c'), Card('8', 'h'), Card('9', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_sequences_in_announcements()

		expected = {BELOTE_TIERCE_STRING : [Card('Q', 'c')],
					BELOTE_QUARTE_STRING : [Card('10', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_two_quartes_of_different_colors_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('10', 'h'), Card('J', 's'), Card('Q', 'h'), Card('K', 's'), Card('Q', 's'), Card('10', 's'), Card('K', 'h'), Card('J', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_sequences_in_announcements()

		expected = {BELOTE_QUARTE_STRING : [Card('K', 's'), Card('K', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_quinta_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('Q', 'h'), Card('7', 's'), Card('10', 'h'), Card('J', 'h'), Card('7', 'c'), Card('9', 'c'), Card('9', 'h'), Card('K', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_sequences_in_announcements()

		expected = {BELOTE_QUINTA_STRING : [Card('K', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_quinta_and_tierce_of_different_colors_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('Q', 'h'), Card('10', 'c'), Card('10', 'h'), Card('J', 'h'), Card('J', 'c'), Card('Q', 'c'), Card('9', 'h'), Card('K', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_sequences_in_announcements()

		expected = {BELOTE_QUINTA_STRING : [Card('K', 'h')],
					BELOTE_TIERCE_STRING: [Card('Q', 'c')]}

		self.assertEqual(expected, player.announcements)



	# def test_with_given_hand_should_set_sequences_in_announcements(self):
	# 	player = Player(name='Player')
	# 	cards = [Card('K','s'), Card('7', 's') , Card('Q', 's'), Card('J', 's'), Card('10' ,'s'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
	# 	player.set_cards(cards)
	# 	player.sort_cards()
		
	# 	player.set_sequences_in_announcements()

	# 	expected = {}

	# 	self.assertEqual(expected, player.announcements[BELOTE_BELOTE_STRING])


if __name__ == '__main__':
	unittest.main()