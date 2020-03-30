import unittest
from team import Team
from player import Player
from card import Card
from belote_constants import *


class TestTeam(unittest.TestCase):
    def test_with_valid_name_and_players(self):
        p1 = Player(name='ime1')
        p2 = Player(name='ime2')

        t = Team('me', p1, p2)

        self.assertEqual(t.name, 'me')

    def test_with_name_bigger_than_10_char_raise_ValueError(self):
        p1 = Player(name='ime1')
        p2 = Player(name='ime2')

        with self.assertRaises(ValueError):
            t = Team('meeeeeeeeeeeee', p1, p2)

    def test_update_points_with_0_points_for_the_first_time(self):
        p1 = Player(name='ime1')
        p2 = Player(name='ime2')
        t = Team('me', p1, p2)

        t.add_points(0)

        self.assertEqual(t.points, [0])


    def test_update_points_twice(self):
        p1 = Player(name='ime1')
        p2 = Player(name='ime2')
        t = Team('me', p1, p2)
        t.add_points(20)

        t.add_points(20)

        self.assertEqual(t.points, [20, 20])

    def test_get_max_tierce(self):
        p1, p2, p3, p4 = Player(name='ime1'), Player(name='ime2'),\
         Player(name='ime3'), Player(name='ime4')
        t1, t2 = Team('prqkor1', p1, p3), Team('prqkor2', p2, p4)
        p1.announcements = {BELOTE_TIERCE_STRING: [Card('9', 's')]}
        p2.announcements = {BELOTE_TIERCE_STRING: [Card('Q', 's')]}
        p3.announcements = {BELOTE_TIERCE_STRING: [Card('A', 's')]}
        p4.announcements = {BELOTE_TIERCE_STRING: [Card('K', 'c')]}

        t1.get_max_tierce()
        t2.get_max_tierce()

        self.assertEqual(t1.highest_tierce, Card('A', 's'))
        self.assertEqual(t2.highest_tierce, Card('K', 'c'))


if __name__ == '__main__':
    unittest.main()
