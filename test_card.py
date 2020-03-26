import unittest
from card import Card

class TestValidateStringCard(unittest.TestCase):
	def test_with_given_non_string_should_return_false(self):
		string_card = 10

		result = Card.validate_string_card(string_card)

		self.assertEqual(False, result)

	def test_with_given_empty_string_should_return_false(self):
		string_card = ''

		result = Card.validate_string_card(string_card)

		self.assertEqual(False, result)

	def test_with_given_invalid_color_string_should_return_false(self):
		string_card = '10b'

		result = Card.validate_string_card(string_card)

		self.assertEqual(False, result)

	def test_with_given_invalid_value_string_should_return_false(self):
		string_card = '11b'

		result = Card.validate_string_card(string_card)

		self.assertEqual(False, result)

	def test_with_given_valid_string_should_return_true(self):
		string_card = '10s'

		result = Card.validate_string_card(string_card)

		self.assertEqual(True, result)


class TestCreatingCardInstance(unittest.TestCase):
	def test_with_given_value_and_color_should_create_instance(self):
		value = '10'
		color = 's'

		card = Card(value, color)
		expected_type = Card
		expected_value = '10'
		expected_color = 's'

		self.assertEqual(expected_type, type(card))
		self.assertEqual(expected_value, card.value)
		self.assertEqual(expected_color, card.color)


class TestFromString(unittest.TestCase):
	def test_with_given_invalid_string_card_should_raise_exception(self):
		string_card = 'as'

		exc = None
		try:
			card = Card.from_string(string_card)
		except Exception as e:
			exc = e 

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid string card given')

	def test_with_given_valid_string_card_should_create_instance(self):
		string_card = 'As'

		card = Card.from_string(string_card)
		expected_type = Card
		expected_value = 'A'
		expected_color = 's'

		self.assertEqual(expected_type, type(card))
		self.assertEqual(expected_value, card.value)
		self.assertEqual(expected_color, card.color)

if __name__ == '__main__':
	unittest.main()