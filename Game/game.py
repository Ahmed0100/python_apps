from player import Player
from board import Board
from round import Round

class Game():
	def __init__(self,id, players):
		self.id = id
		self.players = players
		self.words_used = []
		self.board = board
		self.round = Round(get_word())
		self.player_draw_index = 0
		self.start_new_round()

	def start_new_round(self):
		self.round = Round(self.get_word(),self.players[self.player_draw_index])
		if self.player_draw_index >= len(self.players):
			self.end_round()
			self.end_game()

	def player_guess(self, player, guess):
		pass

	def player_disconnected(self, player):
		pass

	def skip(skielf):
		if self.round:
			n_round = self.round.skip()
			if n_round:
				self.round_ended()
		else:
			raise Exception("No round started yet!")

	def round_ended(self):
		pass

	def update_board(self):
		pass

	def end_game(self):
		pass

	def get_word(self):
		"""gives word that has not been used yet"""
		pass


