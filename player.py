from belote_constants import *
from card import Card

class Player:

	# {'belot':['s','d'],'terca':['K']}

	def __init__(self,*,name):
		assert type(name) == str, 'TypeError'
		self.name = name
		self.cards = []
		self.announcements = {}


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
					for i in range(1,4):
						card_to_check = Card.from_string(BELOTE_ALL_CARDS[pos+8])
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

		for el in self.announcements:
			if el != BELOTE_BELOTE_STRING:
				self.announcements[el] = sorted(self.announcements[el], key=lambda c:Player.modify_card_value(c), reverse = True)		
		



	

