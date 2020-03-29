from player import Player
from team import Team
from round import Round
#from game import Game


def main():
	team1_name = input('Team 1 name: ')
	team2_name = input('Team 2 name: ')

	team1_players=input(team1_name + ' players: ').split(',')
	team2_players=input(team2_name + ' players: ').split(',')



	
	p1 = Player(name = team1_players[0].replace(' ',''))
	p3 = Player(name = team1_players[1].replace(' ',''))

	p1 = Player(name = 'Marto')
	p1 = Player(name = 'Marto')


if __name__ == '__main__':
	main()