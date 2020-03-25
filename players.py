class Player:

	def __init__(self,*,name):
		assert type(name) == str, 'TypeError'
		self.name = name