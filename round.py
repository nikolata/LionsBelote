from croupier import shuffle_list_of_cards


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
        deck = shuffle_list_of_cards()

        start = 0
        end = 8

        for player in self.order:
            player.set_cards(deck[start:end])
            start += 8
            end += 8

            player.sort_cards()
            player.set_announcements()
