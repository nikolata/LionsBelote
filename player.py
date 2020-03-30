from belote_constants import *
from card import Card

class Player:
	def __init__(self,*,name):
		assert type(name) == str, 'TypeError'
		self.name = name
		self.cards = []
		self.announced = {BELOTE_BELOTE_STRING : [],
						  BELOTE_TIERCE_STRING : [],
						  BELOTE_QUARTE_STRING : [], 
						  BELOTE_QUINTA_STRING : [],
						  BELOTE_CARRE_STRING : []}
		self.points = 0
		self.announcements = {}
		self.biggest_sequence = None

	def __repr__(self):
		return self.name

	def set_cards(self, cards):
		self.cards = cards

	def sort_cards(self):
		self.cards = sorted(self.cards)

	def get_belotes(self):
		belotes = []
		for belote in BELOTE_CARDS_FORMING_BELOTE_POSITIONS:
			queen = Card.from_string(BELOTE_ALL_CARDS[belote[0]])
			king = Card.from_string(BELOTE_ALL_CARDS[belote[1]])
			if queen in self.cards and king in self.cards:
				belotes.append(queen.color)
		return belotes

	def arrange_hand_by_color(self, cards=None):
		arranged_cards = []
		current_color = []
		cards_to_arrange = []
		if cards == None:
			cards_to_arrange = self.cards
		else:
			cards_to_arrange = cards
		for card in cards_to_arrange:
			if current_color == []:
				current_color.append(card)
			elif card.color != current_color[0].color:
				arranged_cards.append(current_color)
				current_color = []
				current_color.append(card)
			else:
				current_color.append(card)
		if current_color != []:
			arranged_cards.append(current_color)

		return arranged_cards

	def set_belotes_in_announcements(self):
		belotes = self.get_belotes()
		if belotes != []:
			self.announcements[BELOTE_BELOTE_STRING] = belotes

	def set_given_announcement_in_announcements(self, announcement, card):
		if announcement not in self.announcements.keys():
			self.announcements[announcement] = [card]
		else:
			self.announcements[announcement].append(card)

	def sort_colors_in_hand_by_length(self):
		return sorted(self.arrange_hand_by_color(), key=lambda c:len(c))
		
	def set_all_carres_in_announcements(self):
		colors_by_len = self.sort_colors_in_hand_by_length()
		if len(colors_by_len) == 4:
			elements_to_check = colors_by_len[0]
			for el in elements_to_check:
				is_carre = True
				pos = Card(el.value, 's').get_position()
				if pos not in BELOTE_7S_AND_8S_POSITIONS:
					for i in range(0,4):
						card_to_check = Card.from_string(BELOTE_ALL_CARDS[pos])
						if card_to_check not in self.cards:
							is_carre = False
							break
						pos+=8
					if is_carre:
						self.set_given_announcement_in_announcements(BELOTE_CARRE_STRING, el)


	#use this function only if you have already set carres in announcements!!!
	def find_carre_positions(self):
		postions = []
		if BELOTE_CARRE_STRING in self.announcements:
			for card in self.announcements[BELOTE_CARRE_STRING]:
				current_position = Card(card.value, 's').get_position()
				postions += [current_position, current_position + 8, current_position + 16, current_position + 24]
		return sorted(postions)

	def set_all_sequences_in_announcements(self):
		cards_in_carres = [Card.from_string(BELOTE_ALL_CARDS[pos]) for pos in self.find_carre_positions()]
		cards_to_chech_for_sequence = [card for card in self.cards if card not in cards_in_carres]
		hand = self.arrange_hand_by_color(cards_to_chech_for_sequence)
		for color in hand:
			sequence_length = 1
			last_position = color[0].get_position()

			for i in range(1,len(color)):
				current_card = color[i]
				current_pos = current_card.get_position()-1
				if current_pos == last_position:
					sequence_length += 1
				else:
					if sequence_length == 3:
						self.set_given_announcement_in_announcements(BELOTE_TIERCE_STRING, Card.from_string(BELOTE_ALL_CARDS[last_position]))
					if sequence_length == 4:
						self.set_given_announcement_in_announcements(BELOTE_QUARTE_STRING, Card.from_string(BELOTE_ALL_CARDS[last_position]))
					if sequence_length > 4:
						self.set_given_announcement_in_announcements(BELOTE_QUINTA_STRING, Card.from_string(BELOTE_ALL_CARDS[last_position]))
					sequence_length = 1
				last_position = current_card.get_position()
				

			if sequence_length == 3:
				self.set_given_announcement_in_announcements(BELOTE_TIERCE_STRING, current_card)
			if sequence_length == 4:
				self.set_given_announcement_in_announcements(BELOTE_QUARTE_STRING, current_card)
			if sequence_length > 4:
				self.set_given_announcement_in_announcements(BELOTE_QUINTA_STRING, current_card)

	def modify_card_value(card):
		if card.value == 'J':
			return 11
		if card.value == 'Q':
			return 12
		if card.value == 'K':
			return 13
		if card.value == 'A':
			return 14
		else:
			return int(card.value)

	def set_announcements(self):
		self.set_belotes_in_announcements()
		#the order needs to be this, otherwise it would not work for hand:
		#carre and sequentive cards containing cards from the carre
		self.set_all_carres_in_announcements()
		self.set_all_sequences_in_announcements()

		for announcement in self.announcements:
			if announcement != BELOTE_BELOTE_STRING:
				self.announcements[announcement] = sorted(self.announcements[announcement], key=lambda c:Player.modify_card_value(c), reverse = True)		

	def find_biggest_sequence(self):
		if BELOTE_QUINTA_STRING in self.announcements:
			card = self.announcements[BELOTE_QUINTA_STRING][0]
			return (card.value, 5)
		elif BELOTE_QUARTE_STRING in self.announcements:
			card = self.announcements[BELOTE_QUARTE_STRING][0]
			return (card.value, 4)
		elif BELOTE_TIERCE_STRING in self.announcements:
			card = self.announcements[BELOTE_TIERCE_STRING][0]
			return (card.value, 3)
		return ('7', 0)

	def play_round(self, cards):
		self.set_cards(cards)
		self.sort_cards()
		self.set_announcements()
		self.biggest_sequence = self.find_biggest_sequence()

	def set_points(self):
		belote_pts = 20*len(self.announced[BELOTE_BELOTE_STRING]) 
		tierce_pts = 30*len(self.announced[BELOTE_TIERCE_STRING])
		quarte_pts = 50*len(self.announced[BELOTE_QUARTE_STRING]) 
		quinta_pts = 100*len(self.announced[BELOTE_QUINTA_STRING]) 
		carre_pts = 100*len(self.announced[BELOTE_CARRE_STRING])
		self.points = belote_pts + tierce_pts + quarte_pts + quinta_pts + carre_pts
	
	def set_dict(self):
		self.dict = {
			"cards": self.cards,
			"announcements": self.announced,
			"points": self.points
		}
		return self.dict

	def null_announced_and_points(self):
		self.announcements = {}
		self.announced = {BELOTE_BELOTE_STRING : [],
						  BELOTE_TIERCE_STRING : [],
						  BELOTE_QUARTE_STRING : [], 
						  BELOTE_QUINTA_STRING : [],
						  BELOTE_CARRE_STRING : []}
		self.points = 0

if __name__ == '__main__':
	pl = Player(name='name')
	card_strings = ['10h', 'Qc', 'Ah', 'Ac', 'Jh', 'Kh', 'Kc', 'Qh']
	cards = [Card.from_string(i) for i in card_strings]
	pl.play_round(cards)
	print(pl.biggest_sequence)


	

		