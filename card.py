from belote_constants import *

class Card:

	@staticmethod
	def validate_string_card(string_card):
		if type(string_card) == str:
			if string_card in BELOTE_ALL_CARDS:
				return True 
		return False


	@classmethod
	def from_string(cls, string_card):
		if cls.validate_string_card(string_card):
			color = string_card[-1]
			value = string_card[:-1]
			return cls(value, color)
		raise TypeError('Invalid string card given')


	def __init__(self, value, color):
		self.value = value
		self.color = color

	
	def get_position(self, by_color=True):
		if by_color:
			string_card = self.value+self.color
			return BELOTE_ALL_CARDS.index(string_card)
		else:
			return 	BELOTE_ALL_CARD_VALUES.index(self.value)


	def less_than(self, other):
		return self.get_position(False) < other.get_position(False)

	def __eq__(self, other):
		if other == 0:
			return False
		return self.__dict__ == other.__dict__

	def __lt__(self, other):
		if other == 0:
			return False
		return self.get_position() < other.get_position()

	def __repr__(self):
		return self.value+self.color