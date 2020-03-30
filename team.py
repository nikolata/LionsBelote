from belote_constants import *
from player import Player
from card import Card


class Team:
    def __init__(self, name, p1, p2):
        if len(name)>10:
            raise ValueError
        self.name = name
        self.player1 = p1
        self.player2 = p2
        self.points = None
        self.max_sequence = ('7', 0)
        self.valid_announcements_for_round = {BELOTE_BELOTE_STRING : [],
                                              BELOTE_TIERCE_STRING : [],
                                              BELOTE_QUARTE_STRING : [], 
                                              BELOTE_QUINTA_STRING : [],
                                              BELOTE_CARRE_STRING : []}
    def add_points(self, points):
        if self.points:
            self.points.append(points)
        else:
            self.points = [points]

    def set_dict(self):
        self.dict = {
            self.player1.name: self.player1.set_dict(),
            self.player2.name: self.player2.set_dict()
        }
        return self.dict

    def set_max_sequence(self):
        if self.player1.biggest_sequence == self.player2.biggest_sequence:
            self.max_sequence = self.player1.biggest_sequence
        else:
            if self.player1.biggest_sequence[1] == self.player2.biggest_sequence[1]:
                card_1 = Card(self.player1.biggest_sequence[0], 's')
                card_2 = Card(self.player2.biggest_sequence[0], 's')
                if card_1 > card_2 :
                    self.max_sequence = self.player1.biggest_sequence 
                else:
                 self.max_sequence=self.player2.biggest_sequence
            else:
                if self.player1.biggest_sequence[1] > self.player2.biggest_sequence[1]:
                    self.max_sequence = self.player1.biggest_sequence
                else:
                    self.max_sequence=self.player2.biggest_sequence

    def set_valid_announcements_for_round(self, team_with_max_sequence, trumps):
        if trumps != 'nt':
            self.add_carres()
            if trumps == 'at':
                self.add_belotes()
            else:
                self.add_belotes(color=trumps)

            
            if team_with_max_sequence != 0:
                if self == team_with_max_sequence:
                    self.add_sequences()


    def add_announced(self, string):
        if string in self.player1.announcements:
            self.player1.announced[string] += self.player1.announcements[string]
            self.valid_announcements_for_round[string] += self.player1.announcements[string]
        if string in self.player2.announcements:
            self.player2.announced[string] += self.player2.announcements[string]
            self.valid_announcements_for_round[string] += self.player2.announcements[string]

    def add_carres(self):
        self.add_announced(BELOTE_CARRE_STRING)

    def add_belotes(self, color=None):
        if color == None:
            self.add_announced(BELOTE_BELOTE_STRING)
        else:
            if BELOTE_BELOTE_STRING in self.player1.announcements:
                if self.player1.announcements[BELOTE_BELOTE_STRING] == color:
                    self.player1.announced[BELOTE_BELOTE_STRING] += color
                    self.valid_announcements_for_round[string] += color
            if BELOTE_BELOTE_STRING in self.player2.announcements:
                if self.player2.announcements[BELOTE_BELOTE_STRING] == color:
                    self.player2.announced[BELOTE_BELOTE_STRING] += color
                    self.valid_announcements_for_round[string] += color

    def add_sequences(self):
        self.add_announced(BELOTE_TIERCE_STRING)
        self.add_announced(BELOTE_QUARTE_STRING)
        self.add_announced(BELOTE_QUINTA_STRING)

    def set_points(self):
        self.player1.set_points()
        self.player2.set_points()
        self.add_points(self.player1.points + self.player2.points)

    def null_valid_announcements(self):
        self.player1.null_announced_and_points()
        self.player2.null_announced_and_points()
        self.valid_announcements_for_round = {BELOTE_BELOTE_STRING : [],
                                              BELOTE_TIERCE_STRING : [],
                                              BELOTE_QUARTE_STRING : [], 
                                              BELOTE_QUINTA_STRING : [],
                                              BELOTE_CARRE_STRING : []}
    

    def __eq__(self, other):
        if other == 0 or self ==0:
            return False
        else:
            return self.player1 == other.player1 and self.player2 == other.player2 