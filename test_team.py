import unittest
from team import Team


class Player:
    pass


class TestTeam(unittest.TestCase):
    def test_with_valid_name_and_players(self):
        p1 = Player()
        p2 = Player()

        t = Team('me', p1, p2)

        self.assertEqual(t.name, 'me')


    def test_update_points_with_0_points_for_the_first_time(self):
        p1 = Player()
        p2 = Player()
        t = Team('me', p1, p2)

        t.add_points(0)

        self.assertEqual(t.points, [0])


    def test_update_points_twice(self):
        p1 = Player()
        p2 = Player()
        t = Team('me', p1, p2)
        t.add_points(20)

        t.add_points(20)

        self.assertEqual(t.points, [20, 20])


if __name__ == '__main__':
    unittest.main()
