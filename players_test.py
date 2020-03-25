import unittest
from players import Player

class TestPlayer(unittest.TestCase):
	#
	def test_with_given_no_str_raise_TypeError(self):
		name = 123

		with self.assertRaises(AssertionError):
			p1 = Player(name=name)
	def test_with_given_str_should_create_instance(self):
		name = 'Gosho'

		p1 = Player(name= name)

		self.assertIsNotNone(p1)
		self.assertEqual(name,p1.name)


if __name__ == '__main__':
	unittest.main()