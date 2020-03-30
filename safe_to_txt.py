def create_file_with_headers(team1,team2):
	header = '{:^20}|{:^20}'.format(team1.name,team2.name)
	eq_row = '{:=^41}'.format('=')
	with open("results.txt", "a") as file:
		file.write(header + '\n')
		file.write(eq_row + '\n')

def safe_to_txt(team1,team2,*,first_round = False,last_round = False):	
	if first_round and not last_round:
		first_row = '{:<20}|{:<20}'.format(team1.points[0],team2.points[0])
		with open('results.txt','a') as file:
			file.write(first_row + '\n')
	elif last_round and not first_round:
		all_points_team1 = sum(team1.points) - team1.points[-1]
		all_points_team2 = sum(team2.points) - team2.points[-1]
		team1_string = '{} + {}'.format(all_points_team1,team1.points[-1])
		team2_string = '{} + {}'.format(all_points_team2,team2.points[-1])
		last_row = '{:<20}|{:<20}'.format(sum(team1.points),sum(team2.points))
		with open('results.txt','a') as file:
			file.write(last_row + '\n')
	else:
		all_points_team1 = sum(team1.points) - team1.points[-1]
		all_points_team2 = sum(team2.points) - team2.points[-1]
		team1_string = '{} + {}'.format(all_points_team1,team1.points[-1])
		team2_string = '{} + {}'.format(all_points_team2,team2.points[-1])
		current_row = '{:<20}|{:<20}'.format(team1_string,team2_string)
		with open('results.txt','a') as file:
			file.write(current_row + '\n')

def display_game_points(team1_game_points,team2_game_points):
	if team1_game_points<0 or team2_game_points<0:
		raise ValueError
	if team1_game_points>2 or team2_game_points>2:
		raise ValueError
	eq_row = '{:=^41}'.format('=')
	game_points = '{:^20}|{:^20}'.format('({})'.format(team1_game_points),'({})'.format(team2_game_points))
	with open('results.txt','a') as file:
		file.write(eq_row + '\n')
		file.write(game_points + '\n')
		file.write(eq_row + '\n')
