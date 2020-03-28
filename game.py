from team import Team
from round import Round
import random
class Game:
	def __init__(self,team1,team2):
		self.team1 = team1
		self.team2 = team2
		self.team1_wins = 0
		self.team2_wins = 0
	def play_round(self,last_winner = None):
		if last_winner = team1:
			round.play(player = random.choice([team1.player1,team1.player1]))
		elif last_winner = team2:
			round.play(player = random.choice([team2.player1,team2.player1]))
		else:
			round.play(player = team1.player1)

