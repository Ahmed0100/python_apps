import pygame

class Board():
	ROWS= COLS = 720
	def __init__(self):
		self.create_empty_borad()

	def update(self,x,y,color):
		self.data[y][x] = color

	def clear(self):
		self.create_empty_borad()

	def create_empty_borad(self):
		return self.data = [[(255,255,255) for _ in range(self.COLS)] 
		for _ in range(self.ROWS)]

	def fill(self,x,y):
		pass

	def get_board(self):
		return self.data

