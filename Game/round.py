import time as t
from _threading import *
from game import Game
from chat import Chat
class Round():
	def __init__(self, word, player_drawing, players):

		self.word = word 
		self.player_drawing = player_drawing
		self.player_guessed = []
		self.skips = 0
		self.player_scores = {player:0 for player in players}
		self.time = 75
		start_new_thread(self.time_thread,())
		self.chat = Chat(self)

	def guess(self, player, word):
		correct = word == self.word
		if correct:
			self.player_guessed.append(player)

	def skip(self):
		self.skips+=1
		if self.skips > len(self.players)-2:
			return True
		return False

	def time_thread(self):
		"""
		Runs in a thread to keep track of time
		"""
		while self.time >0:
			t.sleep(1)
			self.time-=1
		self.end_round("Time is up")

	def player_left(self, player):
		if player in self.player_scores:
			del self.player_scores[player]
		if player in self.player_guessed:
			self.player_guessed.remove(player)
		if player == self.player_drawing:
			self.end_round("Drawing player left")

	def end_round(self, msg):
		pass




