import unittest
from safe_to_txt import *
from team import Team
from player import Player
class TestSafeToTxt(unittest.TestCase):
	def test_if_create_file_with_headers_creates_file_with_team_names(self):
		p1 = Player(name ='nikola')
		p3 = Player(name='kolio')
		p2 = Player(name ='kole')
		p4 = Player(name ='niki')

		team1 = Team('mashinite',p1,p3)
		team2 = Team('slabacite',p2,p4)
		create_file_with_headers(team1,team2)
		exp = '     mashinite      |     slabacite      ========================================='
		with open('results.txt', 'r') as file:
			data = file.read().replace('\n','')
		self.assertEqual(data,exp)

	def test_if_safe_to_txt_creates_file_with_headers_and_first_points(self):
		p1 = Player(name ='nikola')
		p3 = Player(name='kolio')
		p2 = Player(name ='kole')
		p4 = Player(name ='niki')

		team1 = Team('mashinite',p1,p3)
		team2 = Team('slabacite',p2,p4)

		team1.add_points(20)
		team2.add_points(0)
		create_file_with_headers(team1,team2)
		safe_to_txt(team1,team2,first_round=True)
		exp = '     mashinite      |     slabacite      =========================================20                  |0                   '

		with open('results.txt', 'r') as file:
			data = file.read().replace('\n','')
		self.assertEqual(data,exp)
	def test_if_safe_to_txt_creates_file_with_headers_and_points(self):
		p1 = Player(name ='nikola')
		p3 = Player(name='kolio')
		p2 = Player(name ='kole')
		p4 = Player(name ='niki')

		team1 = Team('mashinite',p1,p3)
		team2 = Team('slabacite',p2,p4)

		team1.add_points(20)
		team2.add_points(0)
		create_file_with_headers(team1,team2)
		safe_to_txt(team1,team2,first_round=True)
		team1.add_points(40)
		team2.add_points(20)
		safe_to_txt(team1,team2)


		exp = '     mashinite      |     slabacite      =========================================20                  |0                   20 + 40             |0 + 20              '
		with open('results.txt', 'r') as file:
			data = file.read().replace('\n','')
		self.assertEqual(data,exp)
	def test_if_safe_to_txt_creates_file_with_headers_and_final_points(self):
		p1 = Player(name ='nikola')
		p3 = Player(name='kolio')
		p2 = Player(name ='kole')
		p4 = Player(name ='niki')

		team1 = Team('mashinite',p1,p3)
		team2 = Team('slabacite',p2,p4)

		team1.add_points(20)
		team2.add_points(0)
		create_file_with_headers(team1,team2)
		safe_to_txt(team1,team2,first_round=True)
		team1.add_points(40)
		team2.add_points(20)
		safe_to_txt(team1,team2)
		team1.add_points(100)
		team2.add_points(50)
		safe_to_txt(team1,team2,last_round = True)

		exp = '     mashinite      |     slabacite      =========================================20                  |0                   20 + 40             |0 + 20              60 + 100            |20 + 50             160                 |70                  '
		with open('results.txt', 'r') as file:
			data = file.read().replace('\n','')
		self.assertEqual(data,exp)
	def test_with_lower_than_0_team_points_raise_ValueError(self):
		with self.assertRaises(ValueError):
			display_game_points(-3,1)
	def test_with_higher_than_2_team_points_raise_ValueError(self):
		with self.assertRaises(ValueError):
			display_game_points(3,1)
	
	def test_with_given_team_points_create_file_with_correct_pattern(self):
		

		exp = '=========================================        (1)         |        (0)         ========================================='
		open('results.txt','w').close()
		display_game_points(1,0)
		with open('results.txt', 'r') as file:
			data = file.read().replace('\n','')
		self.assertEqual(data,exp)

if __name__ == '__main__':
	unittest.main()