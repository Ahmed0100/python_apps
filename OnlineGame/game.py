import pygame

class Game:
	def __init__(self,id):
		self.p1_moved=False
		self.p2_moved= False
		self.id = id
		self.ready = False
		self.moves = [None,None]
		self.wins=[0,0]

	def get_player_move(self,p):
		return self.moves[p]

	def update_player_move(self,player_id,moves):
		self.moves[player_id] = moves
		if player_id == 0:
			self.p1_moved = True
		else:
			self.p2_moved = True

	def is_connected(self):
		return self.ready

	def is_both_moved(self):
		return self.p1_moved and self.p2_moved

	def get_winner(self):
		p1 = self.moves[0].upper()[0]
		p2 = self.moves[1].upper()[0]
		winner = -1
		if p1 == "R" and p2 =="S":
			winner=0
		elif p1 =="S" and p2 =="R":
			winner = 1
		elif p1 =="P" and p2 =="R":
			winner = 0
		elif p1 =="R" and p2 =="P":
			winner = 1
		elif p1 =="S" and p2 =="P":
			winner = 0
		elif p1 =="P" and p2 =="S":
			winner = 1

		return winner

	def reset_moves(self):
		self.p1_moved = False
		self.p2_moved = False
