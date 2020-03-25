class Player:

	def __init__(self,*,name):
		assert type(name) == str, 'TypeError'
		self.name = name

	def set_cards(self, cards):
		self.cards = cards
