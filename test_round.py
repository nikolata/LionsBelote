import unittest
from round import Round
from team import Team
from player import Player


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


    def test_give_cards_shall_give_eight_cards(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        r = Round(t1, t2)

        r.give_cards()

        self.assertEqual(len(p1.cards), 8)
        self.assertEqual(len(p2.cards), 8)
        self.assertEqual(len(p3.cards), 8)
        self.assertEqual(len(p4.cards), 8)

if __name__ == '__main__':
    unittest.main()
