def create_empty_file():
	open("results.txt", "w").close()

def safe_to_txt(team1,team2,is_this_first_round = False):	
	if is_this_first_round:
		header = '{:^20}|{:^20}'.format(team1.name,team2.name)
		eq_row = '{:=^41}'.format('=')
		print(header)
		print(eq_row)
		first_row = '{:<20}|{:<20}'.format(team1.points[0],team2.points[0])
		print(first_row)
		with open('results.txt','a') as file:
			file.write(header + '\n')
			file.write(eq_row + '\n')
			file.write(first_row + '\n')

	else:
		all_points_team1 = sum(team1.points) - team1.points[-1]
		all_points_team2 = sum(team2.points) - team2.points[-1]
		team1_string = '{} + {}'.format(all_points_team1,team1.points[-1])
		team2_string = '{} + {}'.format(all_points_team2,team2.points[-1])
		current_row = '{:<20}|{:<20}'.format(team1_string,team2_string)
		print(team1.points)

		with open('results.txt','a') as file:
			file.write(current_row + '\n')

def display_game_points(team1_game_points,team2_game_points):
	eq_row = '{:=^41}'.format('=')
	game_points = '{:^20}|{:^20}'.format('({})'.format(team1_game_points),'({})'.format(team2_game_points))
	with open('results.txt','a') as file:
		file.write(eq_row + '\n')
		file.write(game_points + '\n')
		file.write(eq_row + '\n')
