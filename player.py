from belote_constants import *
from card import Card

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
		self.cards = sorted(self.cards)

	def get_belotes(self):
		belotes = []
		for belote in BELOTE_CARDS_FORMING_BELOTE_POSITIONS:
			queen = Card.from_string(BELOTE_ALL_CARDS[belote[0]])
			king = Card.from_string(BELOTE_ALL_CARDS[belote[1]])
			if queen in self.cards and king in self.cards:
				belotes.append(queen.color)
		return belotes

	def arrange_hand_by_color(self):
		arranged_cards = []
		current_color = []
		for card in self.cards:
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
		self.announcements[BELOTE_BELOTE_STRING] = belotes

	def set_given_announcement_in_announcements(self, announcement, card):
		if announcement not in self.announcements.keys():
			self.announcements[announcement] = [card]
		else:
			self.announcements[announcement].append(card)


	def set_all_sequences_in_announcements(self):
		hand = self.arrange_hand_by_color()
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
				pos = el.get_position()
				if pos not in BELOTE_7S_AND_8S_POSITIONS:
					for i in range(1,len(colors_by_len)):
						card_to_check = Card.from_string(BELOTE_ALL_CARDS[pos+8])
						if card_to_check not in colors_by_len[i]:
							is_carre = False
							break
						pos+=8
					if is_carre:
						self.set_given_announcement_in_announcements(BELOTE_CARRE_STRING, el)



	def set_announcements(self):
		self.set_belotes_in_announcements()
		self.set_all_sequences_in_announcements()
		self.set_all_carres_in_announcements()
		for el in self.announcements:
			self.announcements[el] = sorted(self.announcements[el], key=lambda c:c.get_position(), reverse = True)		
		

    # {'belot':['s','d'],'terca':['K']}

    def __init__(self,*,name):
        assert type(name) == str, 'TypeError'
        self.name = name
        self.cards = []
        self.announcements = {}

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

    def arrange_hand_by_color(self):
        arranged_cards = []
        current_color = []
        for card in self.cards:
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
        self.announcements[BELOTE_BELOTE_STRING] = belotes

    def set_given_sequence_in_announcements(self, sequence, card):
        if sequence not in self.announcements.keys():
            self.announcements[sequence] = [card]
        else:
            self.announcements[sequence].append(card)


    def set_sequences_in_announcements(self):
        hand = self.arrange_hand_by_color()
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
                        self.set_given_sequence_in_announcements(BELOTE_TIERCE_STRING, Card.from_string(BELOTE_ALL_CARDS[last_position]))
                    if sequence_length == 4:
                        self.set_given_sequence_in_announcements(BELOTE_QUARTE_STRING, Card.from_string(BELOTE_ALL_CARDS[last_position]))
                    if sequence_length > 4:
                        self.set_given_sequence_in_announcements(BELOTE_QUINTA_STRING, Card.from_string(BELOTE_ALL_CARDS[last_position]))
                    sequence_length = 1
                last_position = current_card.get_position()

            if sequence_length == 3:
                self.set_given_sequence_in_announcements(BELOTE_TIERCE_STRING, current_card)
            if sequence_length == 4:
                self.set_given_sequence_in_announcements(BELOTE_QUARTE_STRING, current_card)
            if sequence_length > 4:
                self.set_given_sequence_in_announcements(BELOTE_QUINTA_STRING, current_card)


    def set_announcements(self):
        self.set_belotes_in_announcements()
        self.set_sequences_in_announcements()
        for el in self.announcements:
            self.announcements[el] = sorted(self.announcements[el], key=lambda r:r.get_position(), reverse = True)      
        

    def __repr__(self):
        return self.name

