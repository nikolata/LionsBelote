from belote_constants import *


class Team:
    def __init__(self, name, p1, p2):
        self.name = name
        self.player1 = p1
        self.player2 = p2
        self.points = None


    def add_points(self, points):
        if self.points:
            self.points.append(points+self.points[-1])
        else:
            self.points = [points]

    def get_max_tierce(self):
        self.player1.get_max_tierce()
        self.player2.get_max_tierce()
        self.highest_tierce = max(self.player1.highest_tierce, self.player2.highest_tierce)


    def erase_tierce_announcements(self):
        self.player1.erase_tierce_announcements()
        self.player2.erase_tierce_announcements()


    def set_dict(self):
        pass

