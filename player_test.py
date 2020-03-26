import unittest
from player import Player

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
		cards = ["7s", "8s", "9s", "10c", "Jd", "Qd", "Kh", "As"]

		player.set_cards(cards)

		self.assertEqual(cards, player.cards)

	def test_sort_cards_should_sort_cards(self):
		player = Player(name='Player')
		cards = ["8s", "7s", "As", "9s", "Jd", "Qd", "10c","Kh"]
		player.set_cards(cards)

		player.sort_cards()
		expected = ["7s", "8s", "9s", "10c", "Jd", "Qd", "Kh", "As"]

		self.assertEqual(expected, player.cards)






if __name__ == '__main__':
	unittest.main()