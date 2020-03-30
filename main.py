from player import Player
from team import Team
from round import Round
from game import Game
from safe_to_txt import *

def main():
	team1_name = input('Team 1 name: ')
	team2_name = input('Team 2 name: ')

	team1_players=input(team1_name + ' players: ').split(',')
	team2_players=input(team2_name + ' players: ').split(',')
	
	p1 = Player(name = team1_players[0].replace(' ',''))
	p3 = Player(name = team1_players[1].replace(' ',''))

	p2 = Player(name = team2_players[0].replace(' ',''))
	p4 = Player(name = team2_players[1].replace(' ',''))

	team1 = Team('Mashinite',p1,p3)
	team2 = Team('Slabacite',p2,p4)
#test

	game = Game(team1,team2)
	while game.team1_wins !=2 and game.team2_wins!=2:
		round_number = 1
		create_file_with_headers(team1,team2)
		is_game_won = False
		game_number = 1
		while not is_game_won:
				game.play_round(round_number)
				if round_number == 1:
					safe_to_txt(team1,team2,first_round = True)
				else:
					safe_to_txt(team1,team2)
				if sum(team1.points)>150 or sum(team2.points)>150 and sum(team1.points) != sum(team2.points):
					is_game_won = True
				# r.print_result()
				print('**********************************')
				
				# print('-----------------')
				# print(team1.points)
				# print(team1.valid_announcements_for_round)
				# print('-----------------')
				# print(team2.points)
				# print(team1.valid_announcements_for_round)

				# print('-----------------')

				round_number +=1
		safe_to_txt(team1,team2,last_round = True)
		if team1.points > team2.points:
			game.team1_wins +=1
			game.last_winner = 'team1'
		elif team1.points<team2.points:
			game.team2_wins +=1
			game.last_winner = 'team2'

		game.team1.points = []
		game.team2.points = []

		# game.set_dict(game_number)
		game_number += 1
		print('-------------------------------NEW GAME----------------------------------------')

		# game.safe_to_txt()
		display_game_points(game.team1_wins,game.team2_wins)

if __name__ == '__main__':
	main()