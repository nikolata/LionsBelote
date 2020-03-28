import unittest
from belote_constants import *
from player import Player
from card import Card
from croupier import shuffle_list_of_cards


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

	def test_get_belotes_with_1_belotes_in_hand_should_return_list_of_one_element_queen_(self):
		player = Player(name='Player')
		cards = [Card('8','s'), Card('7', 's') , Card('A', 's'), Card('K', 'd'), Card('J' ,'d'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
		player.set_cards(cards)

		player.sort_cards()
		result = player.get_belotes()
		expected = ['d']

		self.assertEqual(expected, result)

	def test_get_belotes_with_2_belotes_in_hand_should_return_list_of_two_elements_queens(self):
		player = Player(name='Player')
		cards = [Card('8','s'), Card('7', 's') , Card('Q', 'h'), Card('K', 'd'), Card('J' ,'d'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
		player.set_cards(cards)

		player.sort_cards()
		result = player.get_belotes()
		expected = ['d', 'h']

		self.assertEqual(expected, result)

	def test_get_belotes_with_3_belotes_in_hand_should_return_list_of_three_elements_queens(self):
		player = Player(name='Player')
		cards = [Card('K','s'), Card('7', 's') , Card('Q', 'h'), Card('K', 'd'), Card('Q' ,'s'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
		player.set_cards(cards)

		player.sort_cards()
		result = player.get_belotes()
		expected = ['s', 'd', 'h']

		self.assertEqual(expected, result)

	def test_get_belotes_with_4_belotes_in_hand_should_return_list_of_four_elements_queens(self):
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
	def test_with_given_hand_with_no_belotes_should_do_nothing(self):
		player = Player(name='Player')
		cards = [Card('9','s'), Card('7', 's') , Card('8', 'h'), Card('8', 'd'), Card('Q' ,'s'), Card('Q', 'd'), Card('10', 'c'), Card('K', 'h')]
		player.set_cards(cards)
		player.sort_cards()
		
		player.set_belotes_in_announcements()

		self.assertTrue(BELOTE_BELOTE_STRING not in player.announcements)

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

		player.set_all_sequences_in_announcements()

		expected = {BELOTE_TIERCE_STRING : [Card('K', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_2_tierce_of_one_color_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('A','s'), Card('7', 's') , Card('Q', 's'), Card('K', 's'), Card('9' ,'s'), Card('Q', 'd'), Card('8', 's'), Card('K', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_all_sequences_in_announcements()

		expected = {BELOTE_TIERCE_STRING : [Card('9', 's'), Card('A', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_2_tierce_of_different_colors_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('A','s'), Card('A', 'h') , Card('Q', 's'), Card('K', 's'), Card('Q' ,'h'), Card('Q', 'd'), Card('K', 'h'), Card('10', 'c')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_all_sequences_in_announcements()

		expected = {BELOTE_TIERCE_STRING : [Card('A', 's'), Card('A', 'h')]}

		self.assertEqual(expected, player.announcements)


	def test_with_given_quarte_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('7','h'), Card('8', 'c') , Card('7', 's'), Card('Q', 'h'), Card('A' ,'h'), Card('K', 'h'), Card('9', 'h'), Card('J', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_all_sequences_in_announcements()

		expected = {BELOTE_QUARTE_STRING : [Card('A', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_tierce_and_quarte_of_one_color_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('7','h'), Card('8', 'h') , Card('7', 's'), Card('Q', 'h'), Card('A' ,'h'), Card('K', 'h'), Card('9', 'h'), Card('J', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_all_sequences_in_announcements()

		expected = {BELOTE_TIERCE_STRING : [Card('9', 'h')],
					BELOTE_QUARTE_STRING : [Card('A', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_tierce_and_quarte_of_different_colors_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('10', 'h'), Card('J', 'c'), Card('7', 'h'), Card('9', 'd'), Card('10', 'c'), Card('Q', 'c'), Card('8', 'h'), Card('9', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_all_sequences_in_announcements()

		expected = {BELOTE_TIERCE_STRING : [Card('Q', 'c')],
					BELOTE_QUARTE_STRING : [Card('10', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_two_quartes_of_different_colors_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('10', 'h'), Card('J', 's'), Card('Q', 'h'), Card('K', 's'), Card('Q', 's'), Card('10', 's'), Card('K', 'h'), Card('J', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_all_sequences_in_announcements()

		expected = {BELOTE_QUARTE_STRING : [Card('K', 's'), Card('K', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_quinta_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('Q', 'h'), Card('7', 's'), Card('10', 'h'), Card('J', 'h'), Card('7', 'c'), Card('9', 'c'), Card('9', 'h'), Card('K', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_all_sequences_in_announcements()

		expected = {BELOTE_QUINTA_STRING : [Card('K', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_quinta_and_tierce_of_different_colors_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('Q', 'h'), Card('10', 'c'), Card('10', 'h'), Card('J', 'h'), Card('J', 'c'), Card('Q', 'c'), Card('9', 'h'), Card('K', 'h')]
		player.set_cards(cards)
		player.sort_cards()	
		
		player.set_all_sequences_in_announcements()

		expected = {BELOTE_QUINTA_STRING : [Card('K', 'h')],
					BELOTE_TIERCE_STRING: [Card('Q', 'c')]}

		self.assertEqual(expected, player.announcements)


	#sort_colors_in_hand_by_length
	def test_with_given_one_element_color_should_sort_correctly(self):
		player = Player(name='Player')
		cards = [Card('Q', 'h'), Card('10', 'c'), Card('7', 's'), Card('7', 'h'), Card('10', 'h'), Card('J', 'c'), Card('7', 'c'), Card('7', 'd')]
		player.set_cards(cards)
		player.sort_cards()	

		result = player.sort_colors_in_hand_by_length()

		expected = [[Card('7', 's')], [Card('7', 'd')], [Card('7', 'h'), Card('10', 'h'), Card('Q', 'h')], [Card('7', 'c'), Card('10', 'c'), Card('J', 'c')]]

		self.assertEqual(expected, result)

	def test_with_given_colors_with_more_than_one_element_should_sort_correctly(self):
		player = Player(name='Player')
		cards = [Card('10', 'c'), Card('J', 's'), Card('7', 'c'), Card('9', 's'), Card('8', 'c'), Card('9', 'c'), Card('J', 'c'), Card('Q', 's')]
		player.set_cards(cards)
		player.sort_cards()	

		result = player.sort_colors_in_hand_by_length()

		expected = [[Card('9', 's') ,Card('J', 's'), Card('Q', 's')], [Card('7', 'c'), Card('8', 'c'), Card('9', 'c'), Card('10', 'c'), Card('J', 'c')]]

		self.assertEqual(expected, result)

	def test_with_given_cards_of_one_color_should_sort_correctly(self):
		player = Player(name='Player')
		cards = [Card('10', 'c'), Card('J', 'c'), Card('7', 'c'), Card('9', 'c'), Card('8', 'c'), Card('Q', 'c'), Card('K', 'c'), Card('A', 'c')]
		player.set_cards(cards)
		player.sort_cards()	

		result = player.sort_colors_in_hand_by_length()

		expected = [[Card('7', 'c') ,Card('8', 'c'), Card('9', 'c'), Card('10', 'c'), Card('J', 'c'), Card('Q', 'c'), Card('K', 'c'), Card('A', 'c')]]

		self.assertEqual(expected, result)

	#set_all_carres_in_announcements
	def test_sorry_bro(self):
		player = Player(name='Player')
		player.set_cards(shuffle_list_of_cards()[:8])
		player.sort_cards() 

		player.set_all_carres_in_announcements()

		expected = {}

		self.assertEqual(expected, player.announcements)


	def test_with_given_carre_of_7s_should_do_nothing(self):
		player = Player(name='Player')
		cards = [Card('Q', 'h'), Card('10', 'c'), Card('7', 's'), Card('7', 'h'), Card('10', 'h'), Card('J', 'c'), Card('7', 'c'), Card('7', 'd')]
		player.set_cards(cards)
		player.sort_cards()	

		player.set_all_carres_in_announcements()

		expected = {}

		self.assertEqual(expected, player.announcements)

	def test_with_given_carre_of_8s_should_do_nothing(self):
		player = Player(name='Player')
		cards = [Card('Q', 'h'), Card('10', 'c'), Card('8', 's'), Card('8', 'h'), Card('10', 'h'), Card('J', 'c'), Card('8', 'c'), Card('8', 'd')]
		player.set_cards(cards)
		player.sort_cards()	

		player.set_all_carres_in_announcements()

		expected = {}

		self.assertEqual(expected, player.announcements)

	def test_with_given_cards_of_not_every_color_color_should_do_nothing(self):
		player = Player(name='Player')
		cards = [Card('10', 'c'), Card('J', 'c'), Card('7', 's'), Card('9', 'd'), Card('8', 'c'), Card('Q', 'c'), Card('K', 'c'), Card('A', 'c')]
		player.set_cards(cards)
		player.sort_cards()	

		player.set_all_carres_in_announcements()

		expected = {}

		self.assertEqual(expected, player.announcements)

	def test_with_given_valid_carre_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('Q', 'h'), Card('10', 'c'), Card('9', 's'), Card('9', 'h'), Card('10', 'h'), Card('J', 'c'), Card('9', 'c'), Card('9', 'd')]
		player.set_cards(cards)
		player.sort_cards()	

		player.set_all_carres_in_announcements()

		expected = {BELOTE_CARRE_STRING : [Card('9', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_valid_carre_and_invalid_carre_of_8s_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('8', 'h'), Card('8', 'c'), Card('9', 's'), Card('9', 'h'), Card('8', 'd'), Card('8', 's'), Card('9', 'c'), Card('9', 'd')]
		player.set_cards(cards)
		player.sort_cards()	

		player.set_all_carres_in_announcements()

		expected = {BELOTE_CARRE_STRING : [Card('9', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_2_valid_carres_should_set_correctly(self):
		player = Player(name='Player')
		cards = [Card('J', 'h'), Card('J', 'c'), Card('9', 's'), Card('9', 'h'), Card('J', 'd'), Card('J', 's'), Card('9', 'c'), Card('9', 'd')]
		player.set_cards(cards)
		player.sort_cards()	

		player.set_all_carres_in_announcements()

		expected = {BELOTE_CARRE_STRING : [Card('9', 's'), Card('J', 's')]}

		self.assertEqual(expected, player.announcements)

	#find_carre_positions
	def test_with_given_carre_of_7s_should_return_empty_list(self):
		player = Player(name='Player')
		cards = [Card('Q', 'h'), Card('10', 'c'), Card('7', 's'), Card('7', 'h'), Card('10', 'h'), Card('J', 'c'), Card('7', 'c'), Card('7', 'd')]
		player.set_cards(cards)
		player.sort_cards()	
		player.set_all_carres_in_announcements()

		result = player.find_carre_positions()
		expected = []

		self.assertEqual(expected, result)

	def test_with_given_carre_of_8s_should_return_empty_list(self):
		player = Player(name='Player')
		cards = [Card('Q', 'h'), Card('10', 'c'), Card('8', 's'), Card('8', 'h'), Card('10', 'h'), Card('J', 'c'), Card('8', 'c'), Card('8', 'd')]
		player.set_cards(cards)
		player.sort_cards()	
		player.set_all_carres_in_announcements()

		result = player.find_carre_positions()
		expected = []

		self.assertEqual(expected, result)

	def test_with_given_cards_of_not_every_color_color_should_print_empty_list(self):
		player = Player(name='Player')
		cards = [Card('10', 'c'), Card('J', 'c'), Card('7', 's'), Card('9', 'd'), Card('8', 'c'), Card('Q', 'c'), Card('K', 'c'), Card('A', 'c')]
		player.set_cards(cards)
		player.sort_cards()	
		player.set_all_carres_in_announcements()

		result = player.find_carre_positions()
		expected = []

		self.assertEqual(expected, result)

	def test_with_given_valid_carre_should_return_list_with_correct_positions(self):
		player = Player(name='Player')
		cards = [Card('Q', 'h'), Card('10', 'c'), Card('9', 's'), Card('9', 'h'), Card('10', 'h'), Card('J', 'c'), Card('9', 'c'), Card('9', 'd')]
		player.set_cards(cards)
		player.sort_cards()	
		player.set_all_carres_in_announcements()

		result = player.find_carre_positions()
		expected = [2, 10, 18, 26]

		self.assertEqual(expected, result)

	def test_with_given_valid_carre_and_invalid_carre_of_8s_should_return_list_with_correct_positions(self):
		player = Player(name='Player')
		cards = [Card('8', 'h'), Card('8', 'c'), Card('9', 's'), Card('9', 'h'), Card('8', 'd'), Card('8', 's'), Card('9', 'c'), Card('9', 'd')]
		player.set_cards(cards)
		player.sort_cards()	
		player.set_all_carres_in_announcements()

		result = player.find_carre_positions()
		expected = [2, 10, 18, 26]

		self.assertEqual(expected, result)

	def test_with_given_2_valid_carres_should_return_list_with_correct_positions(self):
		player = Player(name='Player')
		cards = [Card('J', 'h'), Card('J', 'c'), Card('9', 's'), Card('9', 'h'), Card('J', 'd'), Card('J', 's'), Card('9', 'c'), Card('9', 'd')]
		player.set_cards(cards)
		player.sort_cards()	
		player.set_all_carres_in_announcements()

		result = player.find_carre_positions()
		expected = [2, 4, 10, 12, 18, 20, 26, 28]

		self.assertEqual(expected, result)


	#set_announcements
	def test_with_given_hand_with_no_announcements_should_do_nothing(self):
		player = Player(name='Player')
		card_strings = ['7s', '8c', '7c', 'Jh', '9s', '10d', 'Ad', 'Kc']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_belote_only_should_set_only_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['7s', '8c', '7c', 'Qc', '9s', '10d', 'Ad', 'Kc']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['c']}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_two_belotes_should_set_belotes_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['7s', '8c', 'Qd', 'Qc', '9s', '10d', 'Kd', 'Kc']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['d', 'c']}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_four_belotes_should_set_belotes_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Qs', 'Ks', 'Qd', 'Qc', 'Qh', 'Kh', 'Kd', 'Kc']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['s', 'd', 'h', 'c'],
					BELOTE_CARRE_STRING : [Card('K', 's'), Card('Q', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_only_tierce_should_set_only_tierce_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Js', '9s', '7h', '8c', 'Qc', 'Kh', '10s', 'Ac']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_TIERCE_STRING : [Card('J', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_only_tierce_major_should_set_tierce_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Qs', '9s', '7h', '8c', 'Qc', 'Kh', 'Ks', 'As']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['s'], 
					BELOTE_TIERCE_STRING : [Card('A', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_tierce_and_belote_from_same_color_should_set_tierce_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['7s', '9s', '7h', '8s', 'Qs', 'Kh', 'Ks', 'Qc']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['s'], 
					BELOTE_TIERCE_STRING : [Card('9', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_tierce_and_belote_from_different_colors_should_set_tierce_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['7s', '9s', '7h', '8s', 'Qd', 'Kc', 'Ks', 'Qc']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['c'], 
					BELOTE_TIERCE_STRING : [Card('9', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_tierce_major_and_belote_should_set_tierce_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Qs', '9s', '7h', '8c', 'Qc', 'Kc', 'Ks', 'As']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['s', 'c'], 
					BELOTE_TIERCE_STRING : [Card('A', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_tierce_and_two_belotes_one_from_the_tierce_color_should_set_tierce_and_belotes_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['8s', '9s', 'Qc', 'Qs', 'Kc', '10s', 'Ah', 'Ks']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['s', 'c'], 
					BELOTE_TIERCE_STRING : [Card('10', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_tierce_and_two_belotes_not_from_the_tierce_color_should_set_tierce_and_belotes_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['8s', '9s', 'Qc', 'Qd', 'Kc', '10s', 'Ah', 'Kd']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['d', 'c'], 
					BELOTE_TIERCE_STRING : [Card('10', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_tierce_major_and_two_belotes_should_set_tierce_and_belotes_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Qc', '7d', 'Qs', 'Kh', 'Ks', 'Qh', 'Kc', 'As']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['s', 'h', 'c'], 
					BELOTE_TIERCE_STRING : [Card('A', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_two_tierces_of_one_color_one_major_should_set_tierces_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Qd', '7d', '8d', 'Ac', 'Jd', '9d', 'Kh', 'Kd']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['d'], 
					BELOTE_TIERCE_STRING : [Card('K', 'd'), Card('9', 'd')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_two_tierces_of_different_colors_should_set_tierces_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Js', '7d', '8d', '10s', 'Ac', '9d', 'Kh', '9s']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_TIERCE_STRING : [Card('J', 's'), Card('9', 'd')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_two_tierces_of_different_colors_and_belote_from_third_color_should_set_tierces_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Js', '7d', '8d', '10s', 'Qc', '9d', 'Kc', '9s']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['c'],
					BELOTE_TIERCE_STRING : [Card('J', 's'), Card('9', 'd')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_two_major_tierces_of_and_belote_should_set_tierces_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Kh', 'Qs', 'Ks', 'Qh', 'Ac', 'As', 'Qc', 'Kc']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['s', 'h',  'c'],
					BELOTE_TIERCE_STRING : [Card('A', 's'), Card('A', 'c')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_quarte_with_belote_should_set_quarte_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['9h', '9s', 'Kd', '8s', 'Qd', '10s', '8h', 'Js']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['d'],
					BELOTE_QUARTE_STRING : [Card('J', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_quarte_with_belote_in_quarte_should_set_quarte_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Jh', '9s', 'Ad', '7s', 'Qd', '8d', 'Kd', 'Jd']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['d'],
					BELOTE_QUARTE_STRING : [Card('A', 'd')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_quarte_with_belote_from_same_color_but_not_in_quarte_should_set_quarte_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['10d', '9d', '8d', '7d', 'Qd', 'As', 'Kd', 'Ah']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['d'],
					BELOTE_QUARTE_STRING : [Card('10', 'd')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_quarte_and_tierce_major_should_set_quarte_tierce_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['10d', '9d', '8d', 'Ah', 'Qs', 'Jd', 'As', 'Ks']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['s'],
					BELOTE_TIERCE_STRING : [Card('A', 's')],
					BELOTE_QUARTE_STRING : [Card('J', 'd')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_quarte_and_tierce_major_and_belote_in_guarte_should_set_quarte_tierce_and_belotes_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['8c', '10h', 'Qc', 'Qh', 'Jh', 'Ac', 'Kc', 'Kh']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['h', 'c'],
					BELOTE_TIERCE_STRING : [Card('A', 'c')],
					BELOTE_QUARTE_STRING : [Card('K', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_quarte_and_tierce_from_one_color_and_belote_in_guarte_should_set_quarte_tierce_and_belotes_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['8h', 'Jc', 'Qc', 'Jd', 'Kd', 'Kc', 'Ac', 'Qd']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['d', 'c'],
					BELOTE_TIERCE_STRING : [Card('K', 'd')],
					BELOTE_QUARTE_STRING : [Card('A', 'c')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_two_quartes_and_belotes_in_guartes_should_set_quartes_and_belotes_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Js', 'Qh', 'Jh', 'Ks', 'Qs', 'Ah', 'Kh', 'As']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['s', 'h'],
					BELOTE_QUARTE_STRING : [Card('A', 's'), Card('A', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_quinta_and_belote_in_guinta_should_set_quinta_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['8s', '7c', '9s', 'Ks', 'Qs', 'Ad', '10s', 'Js']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['s'],
					BELOTE_QUINTA_STRING : [Card('K', 's')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_quinta_and_belote_in_guinta_and_tierce_major_should_set_quinta_tierce_and_belotes_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['10h', 'Qc', 'Ah', 'Ac', 'Jh', 'Kh', 'Kc', 'Qh']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
		expected = {BELOTE_BELOTE_STRING : ['h', 'c'],
					BELOTE_TIERCE_STRING : [Card('A', 'c')],
					BELOTE_QUINTA_STRING : [Card('A', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_carre_and_belote_should_set_carre_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Qd', 'Qs', 'Qc', '7c', 'Ks', 'Qh', 'Ad', '8c']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
	
		expected = {BELOTE_BELOTE_STRING : ['s'],
					BELOTE_CARRE_STRING : [Card('Q', 'h')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_carre_and_valid_tierce_major_should_set_carre_tierce_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['9s', 'As', '9c', '9h', 'Ks', '9d', 'Qs', '7c']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
	
		expected = {BELOTE_BELOTE_STRING : ['s'],
					BELOTE_TIERCE_STRING : [Card('A', 's')],
					BELOTE_CARRE_STRING : [Card('9', 'd')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_carre_and_invalid_tierce_major_should_set_carre_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['8s', 'As', 'Qc', 'Qh', 'Ks', 'Qd', 'Qs', '7c']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
	
		expected = {BELOTE_BELOTE_STRING : ['s'],
					BELOTE_CARRE_STRING : [Card('Q', 'd')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_carre_and_valid_quarte_with_belote_in_quarte_should_set_carre_quarte_and_belote_in_announcements(self):
		player = Player(name='Player')
		card_strings = ['Js', 'As', '9c', '9h', 'Ks', '9d', 'Qs', '9s']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
	
		expected = {BELOTE_BELOTE_STRING : ['s'],
					BELOTE_QUARTE_STRING : [Card('A', 's')],
					BELOTE_CARRE_STRING : [Card('9', 'd')]}

		self.assertEqual(expected, player.announcements)

	def test_with_given_hand_with_carre_and_invalid_quarte_with_belote_in_quarte_should_set_correctly_in_announcements(self):
		player = Player(name='Player1')
		player_2 = Player(name='Player2')
		card_strings = ['Js', 'As', 'Jc', 'Jh', 'Ks', 'Jd', 'Qs', '7c']
		card_strings_2 = ['Js', 'As', 'Qc', 'Qh', 'Ks', 'Qd', 'Qs', '7c']
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player_2.set_cards([Card.from_string(i) for i in card_strings_2])
		player.sort_cards()	
		player_2.sort_cards()

		player.set_announcements()
		player_2.set_announcements()
	
		expected = {BELOTE_BELOTE_STRING : ['s'],
					BELOTE_TIERCE_STRING : [Card('A', 's')],
					BELOTE_CARRE_STRING : [Card('J', 'd')]}

		expected_2 = {BELOTE_BELOTE_STRING : ['s'],
					BELOTE_CARRE_STRING : [Card('Q', 'd')]}

		self.assertEqual(expected, player.announcements)
		self.assertEqual(expected_2, player_2.announcements)

	def test_with_given_perfect_hand_should_set_correctly_in_announcements(self):
		player = Player(name='Player1')		
		card_strings = ['Js', '9s', 'Jc', 'Jh', '9c', 'Jd', '9h', '9d']		
		player.set_cards([Card.from_string(i) for i in card_strings]) 
		player.sort_cards()	

		player.set_announcements()
			
		expected = {BELOTE_CARRE_STRING : [Card('J', 's'), Card('9', 's')]}	

		self.assertEqual(expected, player.announcements)	


if __name__ == '__main__':
	unittest.main()