from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from person import Person
import time 

PORT = 5050
HOST = 'localhost'
ADDR = (HOST,PORT)
HEADER = 64
FORMAT ="utf8"
BUFSIZE = 512
SERVER = socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADDR)

persons = []

def broadcast(msg, name):
	for person in persons:
		client = person.client
		try:
			client.send(bytes(name,FORMAT)+msg)
		except Exception as e:
			print("[Exception]",e)

def client_communication(person):
	client = person.client
	name = client.recv(BUFSIZE).decode(FORMAT)
	person.set_name(name)
	msg = bytes(f"{name} has joined the chat",FORMAT)

	broadcast(msg,"")
	while True:
		message = client.recv(BUFSIZE)
		if message == bytes("quit",FORMAT):
			client.close()
			persons.remove(person)
			broadcast(bytes(f"{name} has left the chat",FORMAT), "")
			print(f"[DISCONNECTED] {person.name} disconnected")
			break
		else:
			broadcast(message,name +": ")
			print(f"{name}: ",msg.decode(FORMAT))

def wait_for_connection():
	while True:
		try:
			client,client_addr = SERVER.accept()
			person = Person(client_addr,client)
			persons.append(person)
			print(f"[CONNECTION] {client_addr} connected to the server at {time.time()}")

			Thread(target=client_communication, args=(person,)).start()
		except Exception as e:
			print("Exception",e)
			break
	print("SERVER CRASHED")

if __name__ == "__main__":
	SERVER.listen(5) #listen to 5 connections
	print("[STARTED] Waiting for connections")
	ACCEPT_THREAD = Thread(target=wait_for_connection)
	ACCEPT_THREAD.start()
	ACCEPT_THREAD.join()
	SERVER.close()