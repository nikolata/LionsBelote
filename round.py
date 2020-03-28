from croupier import shuffle_list_of_cards, set_type_of_game
from belote_constants import *


class Round:
    def __init__(self, t1, t2):
        self.team1 = t1
        self.team2 = t2
        self.order = [self.team1.player1, self.team2.player1,\
         self.team1.player2, self.team2.player2]
        self.team1.set_dict()
        self.team2.set_dict()
        self.tierce = {}
        self.quarte = {}
        self.quinte = {}

        # self.dict = {
        #     self.team1.name: {
        #         self.team1.player1.name: {
        #             "cards": None,
        #             "announcements": None,
        #             "points": None
        #         }
        #     }
        # }

# "Mecheta": {
#     "Marto": {
#         "cards:": ["7s", "8s", "9s", "10c", "Jd", "Qd", "Kh", "As"],
#         "announcements": ["tierce"],
#         "points": 20
#     },
#     "Rado": {
#         "cards:": ["7d", "8c", "9d", "10d", "Js", "Qs", "Kd", "Ac"],
#         "announcements": [],
#         "points": 0
#     }
# },
# "Koteta": {
#     "Gosho": {
#         "cards:": ["7c", "8d", "9c", "10s", "Jh", "Qc", "Kc", "Ad"],
#         "announcements": [],
#         "points": 0
#     },
#     "Pesho": {
#         "cards:": ["7h", "8h", "9h", "10h", "Jc", "Qh", "Ks", "Ah"],
#         "announcements": ["quarte"],
#         "points": 50
#     }
# }

    def play(self, player=None):
        self.set_order(player)
        self.set_trumps()
        self.give_cards()
        for _ in range(4):
            pass

        # save_round_to_txt


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

                # print(player, ' : ', player.cards)
                # print('deck: ', deck)

                player.sort_cards()
                player.set_announcements()

                if BELOTE_BELOTE_STRING in player.announcements:
                    self.check_belote(player)

        # else:
        #     add_points(0)


    def check_belote(self, player):
        player_belote_announcements = player.announcements[BELOTE_BELOTE_STRING]

        if self.trumps == 'at':
            for i in range(len(player_belote_announcements) - 1):
                player_belote_announcements.pop()
        else:
            for belote in player_belote_announcements:
                if belote != self.trumps:
                    player_belote_announcements.remove(belote)


    def check_tierce(self):
        self.team1.get_max_tierce()
        self.team2.get_max_tierce()
        if self.team2.highest_tierce and self.team1.highest_tierce:
            if self.team2.highest_tierce.less_than(self.team1.highest_tierce):
                self.team2.erase_tierce_announcements()
            elif self.team1.highest_tierce.less_than(self.team2.highest_tierce):
                self.team1.erase_tierce_announcements()


    def set_trumps(self):
        self.trumps = set_type_of_game()
