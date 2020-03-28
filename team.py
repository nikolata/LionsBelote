class Team:
    def __init__(self, name, p1, p2):
        self.name = name
        self.player1 = p1
        self.player2 = p2
        self.points = None


    def add_points(self, points):
        if self.points:
            self.points.append(points)
        else:
            self.points = [points]