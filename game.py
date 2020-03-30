from team import Team
from round import Round
import random
import json
class Game:
	def __init__(self,team1,team2):
		self.team1 = team1
		self.team2 = team2
		self.team1_wins = 0
		self.team2_wins = 0
		self.last_winner = None
		self.game_dict = {}
		self.games_dict = {}
	def play_round(self,round_num = 1):
		r = Round(round_num,self.team1,self.team2)
		if self.last_winner == 'team1':
			r.play(player = random.choice([self.team1.player1,self.team1.player1]))
		elif self.last_winner == 'team2':
			r.play(player = random.choice([self.team2.player1,self.team2.player1]))
		else:
			r.play(player = self.team1.player1)

		round_n = 'round ' + str(round_num) 
		self.game_dict.update({round_n: r.set_dict()})
	def set_dict(self,game_num=1):
		game_n = 'game ' + str(game_num)
		self.games_dict.update({game_n: self.game_dict})
	#	print(self.games_dict)
	def safe_to_json(self):
		with open('data.json', 'w') as file:
				json.dump(self.games_dict,file,indent = 4)
