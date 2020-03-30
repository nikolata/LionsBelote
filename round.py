from croupier import shuffle_list_of_cards, set_type_of_game
from belote_constants import *
from player import Player
from team import Team
from card import Card


class Round:
    def __init__(self, number, t1, t2):
        self.number = number
        self.team1 = t1
        self.team2 = t2
        self.order = [self.team1.player1, self.team2.player1,\
         self.team1.player2, self.team2.player2]
        self.tierce = {}
        self.quarte = {}
        self.quinte = {}
        self.trumps = ''


    def set_dict(self):
        self.dict = {
            self.team1.name: self.team1.set_dict(),
            self.team2.name: self.team2.set_dict(),
            "trumps": self.trumps
        }
        return self.dict


    def play(self, player=None):
        self.set_order(player)
        self.set_trumps()
        cards_for_round = shuffle_list_of_cards()
        self.check_announcements(cards_for_round)    
        team_with_max_sequence = self.find_team_with_biggest_sequence()
        self.team1.set_valid_announcements_for_round(team_with_max_sequence, self.trumps)
        self.team2.set_valid_announcements_for_round(team_with_max_sequence, self.trumps)
        self.team1.set_points()
        self.team2.set_points()
        
    def empty_announcements(self):
        self.team1.null_valid_announcements()
        self.team2.null_valid_announcements()


    def set_order(self, player=None):
        if not player:
            player = self.order[0]
        self.on_turn = player


    def next_order(self):
        try:
            self.set_order(self.order[self.order.index(self.on_turn)+1])
        except IndexError:
            self.set_order()

    def check_announcements(self, cards):
        self.team1.player1.play_round(cards[0:8])
        self.team1.player2.play_round(cards[8:16])
        self.team2.player1.play_round(cards[16:24])
        self.team2.player2.play_round(cards[24:32])

    def find_team_with_biggest_sequence(self):
        self.team1.set_max_sequence()
        self.team2.set_max_sequence()
        seq_1 = self.team1.max_sequence
        seq_2 = self.team2.max_sequence
        if seq_1 == seq_2:
            return 0
        else:
            if seq_1[1] == seq_2[1]:
                card_1 = Card(seq_1[0], 's')
                card_2 = Card(seq_2[0], 's')
                if card_1 > card_2 :
                     return self.team1
                else:
                 return self.team2
            else:
                if seq_1[1] > seq_2[1]:
                    return self.team1
                else:
                    return self.team2

    def set_trumps(self):
        self.trumps = set_type_of_game()

    def print_result(self):
        print('Team1: ',self.team1.valid_announcements_for_round)
        print('PLayer1: ', self.team1.player1.announced)
        print('Player2: ', self.team1.player2.announced)
        print('Points: ',self.team1.points)
        print('=================================================')
        print('Team2: ', self.team2.valid_announcements_for_round)
        print('PLayer1: ', self.team2.player1.announced)
        print('Player2: ', self.team2.player2.announced)
        print('Points: ', self.team2.points)

