from croupier import shuffle_list_of_cards, set_type_of_game
from belote_constants import *


class Round:
    def __init__(self, t1, t2):
        self.team1 = t1
        self.team2 = t2
        self.order = [self.team1.player1, self.team2.player1,\
         self.team1.player2, self.team2.player2]


    def set_order(self, player=None):
        if not player:
            player = self.order[0]
        self.on_turn = player


    def next_order(self):
        try:
            self.set_order(self.order[self.order.index(self.on_turn)+1])
        except IndexError:
            self.set_order()


    def give_cards(self):

        if self.trumps != 'nt':

            deck = shuffle_list_of_cards()

            start = 0
            end = 8

            for player in self.order:
                player.set_cards(deck[start:end])
                start += 8
                end += 8

                player.sort_cards()
                player.set_announcements()

                self.check_announcements(player)

        # else:
        #     add_points(0)


    def check_announcements(self, player):
        self.check_belote(player)


    def check_belote(self, player):
        if self.trumps == 'at':
            for i in range(len(player.announcements[BELOTE_BELOTE_STRING]) - 1):
                player.announcements[BELOTE_BELOTE_STRING].pop()
        else:
            for belote in player.announcements[BELOTE_BELOTE_STRING]:
                if belote != self.trumps:
                    player.announcements[BELOTE_BELOTE_STRING].remove(belote)


    def set_trumps(self, trumps):
        self.trumps = set_type_of_game()
