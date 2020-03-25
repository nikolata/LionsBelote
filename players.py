class Player:

	def __init__(self,*,name):
		assert type(name) == str, 'TypeError'
		self.name = name
		self.cards = []
		self.announcements = {'belot':['s','d'],'terca':['K']}


	def set_cards(self, cards):
		self.cards = cards

	def antoni_foo():
		pass

