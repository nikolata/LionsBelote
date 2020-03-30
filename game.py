from team import Team
from round import Round
import random
class Game:
	def __init__(self,team1,team2):
		self.team1 = team1
		self.team2 = team2
		self.team1_wins = 0
		self.team2_wins = 0
		self.last_winner = None
		self.dict = {}
	def play_round(self,round_num = 1):
		r = Round(round_num,self.team1,self.team2)
		if self.last_winner == 'team1':
			r.play(player = random.choice([team1.player1,team1.player1]))
		elif self.last_winner == 'team2':
			r.play(player = random.choice([team2.player1,team2.player1]))
		else:
			r.play(player = team1.player1)


	def set_dict(self, round):
		self.dict.append(round.number: round.set_dict())
