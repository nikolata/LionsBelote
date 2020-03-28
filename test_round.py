import unittest
from round import Round
from team import Team
from player import Player
from belote_constants import *
from card import Card


class TestRound(unittest.TestCase):
    def test_initializing_round(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)

        r = Round(t1, t2)

        self.assertIsNotNone(r)


    def test_set_order_order(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)

        r.set_order(p4)

        self.assertEqual(r.order, [p1, p2, p3, p4])


    def test_set_order_with_nothing(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)

        r.set_order()

        self.assertEqual(r.on_turn, p1)


    def test_set_order_with_player(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)

        r.set_order(p4)

        self.assertEqual(r.on_turn, p4)


    def test_next_order_on_first_element(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)
        r.set_order()

        r.next_order()
        r.next_order()

        self.assertEqual(r.on_turn, p3)


    def test_next_order_on_last_element(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)
        r.set_order(p4)

        r.next_order()

        self.assertEqual(r.on_turn, p1)


    # def test_give_cards_shall_give_eight_cards(self):
    #     p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
    #      Player(name='ime3'), Player(name='ime4')
    #     t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
    #     r = Round(t1, t2)
    #     r.trumps = 'at'

    #     r.give_cards()

    #     self.assertEqual(len(p1.cards), 8)
    #     self.assertEqual(len(p2.cards), 8)
    #     self.assertEqual(len(p3.cards), 8)
    #     self.assertEqual(len(p4.cards), 8)


    def test_give_cards_with_no_trumps_should_not_set_announcements(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)
        r.trumps = 'nt'

        r.give_cards()

        self.assertEqual(len(p1.cards), 0)
        self.assertEqual(len(p2.cards), 0)
        self.assertEqual(len(p3.cards), 0)
        self.assertEqual(len(p4.cards), 0)


    def test_iterate_round(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)
        r.trumps = 'nt'

        r.play()

        


class TestRoundCheckAnnouncements(unittest.TestCase):
    # check belote
    def test_with_belote_on_trump_should_not_change(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)
        p1.announcements = {BELOTE_BELOTE_STRING: ['h']}
        r.trumps = 'h'

        r.check_belote(p1)

        self.assertEqual(p1.announcements, {BELOTE_BELOTE_STRING: ['h']})


    def test_with_belote_not_on_trump_should_go_away(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)
        p1.announcements = {BELOTE_BELOTE_STRING: ['h']}
        r.trumps = 's'

        r.check_belote(p1)

        self.assertEqual(p1.announcements, {BELOTE_BELOTE_STRING: []})


    def test_with_belote_on_all_trumps_should_only_one_stay(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)
        p1.announcements = {BELOTE_BELOTE_STRING: ['h', 's', 'c', 'd']}
        r.trumps = 'at'

        r.check_belote(p1)

        self.assertEqual(len(p1.announcements[BELOTE_BELOTE_STRING]), 1)

    #check tierce
    def test_with_first_team_low_tierce_second_team_high_tierce_should_only_second_stay(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)
        p1.announcements = {BELOTE_TIERCE_STRING: [Card('9', 's')]}
        p2.announcements = {BELOTE_TIERCE_STRING: [Card('Q', 's')]}

        r.check_tierce()

        self.assertNotIn(BELOTE_TIERCE_STRING, p1.announcements.keys())
        self.assertEqual(p2.announcements[BELOTE_TIERCE_STRING], [Card('Q', 's')])


    def test_with_four_tierce(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)
        p1.announcements = {BELOTE_TIERCE_STRING: [Card('9', 's')]}
        p2.announcements = {BELOTE_TIERCE_STRING: [Card('Q', 's')]}
        p3.announcements = {BELOTE_TIERCE_STRING: [Card('A', 's')]}
        p4.announcements = {BELOTE_TIERCE_STRING: [Card('K', 'c')]}

        r.check_tierce()

        self.assertEqual(p1.announcements[BELOTE_TIERCE_STRING], [Card('9', 's')])
        self.assertNotIn(BELOTE_TIERCE_STRING, p2.announcements.keys())
        self.assertEqual(p3.announcements[BELOTE_TIERCE_STRING], [Card('A', 's')])
        self.assertNotIn(BELOTE_TIERCE_STRING, p4.announcements.keys())


    def test_with_one_tierce(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)
        p1.announcements = {BELOTE_TIERCE_STRING: [Card('9', 's')]}
        p2.announcements = {}
        p3.announcements = {}
        p4.announcements = {}

        r.check_tierce()

        self.assertEqual(p1.announcements[BELOTE_TIERCE_STRING], [Card('9', 's')])
        self.assertNotIn(BELOTE_TIERCE_STRING, p2.announcements.keys())
        self.assertNotIn(BELOTE_TIERCE_STRING, p3.announcements.keys())
        self.assertNotIn(BELOTE_TIERCE_STRING, p4.announcements.keys())



if __name__ == '__main__':
    unittest.main()
