import socket
import time
from _thread import *
import sys
from player import Player
import pickle
from game import Game

SERVER = "localhost"
PORT = 5555

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
	sock.bind((SERVER,PORT))
except socket.error as e:
	str(e)

sock.listen(2)
print("Waiting for connection. Server Started")

connected = set()
games = { }
id_count = 0

def threaded_client(conn,player_id, game_id):
	global id_count
	conn.send(str.encode(str(player_id)))
	reply = ""
	while True:
		try:
			data = conn.recv(4096).decode()
			if game_id in games:
				game= games[game_id]
				if not data:
					break
				else:
					if data == "reset":
						game.reset_moves()
					elif data != "get":
						game.update_player_move(player_id,data)
					conn.sendall(pickle.dumps(game))
			else:
				break
		except:
			print("exception")
			break
	print("Lost Connection")
	try:
		del games[game_id]
		print("Closing Game", game_id)
	except:
		pass
	id_count -= 1
	conn.close()
currPlayer = 0;
while(True):
	conn, addr = sock.accept()
	print("Connected to:",addr)
	id_count += 1
	p = 0
	game_id = (id_count-1)//2
	if id_count % 2 == 1:
		games[game_id] = Game(game_id)
		print("Creating a new game", game_id)
	else:
		games[game_id].ready = True
		p = 1
	start_new_thread(threaded_client, (conn,p, game_id))
