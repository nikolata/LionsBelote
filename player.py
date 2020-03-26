class Player:

	# {'belot':['s','d'],'terca':['K']}


	def __init__(self,*,name):
		assert type(name) == str, 'TypeError'
		self.name = name
		self.cards = []
		self.announcements = {}

	def set_cards(self, cards):
		self.cards = cards

	def sort_cards(self):
		pass

	

