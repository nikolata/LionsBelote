#from team import Team
from tabulate import tabulate
def safe_to_txt(is_this_first_round = True):
	team1_name = 'mecheta'
	team2_name = 'koteta'
	all_points_team1 = 0
	all_points_team2 = 0
	points_this_round_team1 =0
	points_this_round_team2 =0
	
	table = []
	headers = [team1_name, team2_name]


	first_row  = [points_this_round_team1 ,points_this_round_team2]
	table.append(first_row)

	current_row = ['{} + {}'.format(all_points_team1,20),'{} + {}'.format(all_points_team2,0)]
	table.append(current_row)
	current_row = ['{} + {}'.format(20,100),'{} + {}'.format(0,20)]
	table.append(current_row)	
	tab = tabulate(table, headers, tablefmt="github")
	print(tab)
	with open('results.txt','w') as file:
		file.write(tab)

	game_points1 = 0
	game_points2 = 1
	game = []
	game.append(['(0)','(1)'])
	#use this for the final
	g = tabulate(game, tablefmt="psql")
	print(g)
	with open('results.txt','w') as file:
		file.write(tab + '\n')

	with open('results.txt','a') as file:
		file.write(g)
safe_to_txt()
