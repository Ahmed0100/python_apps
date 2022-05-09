from client import Client
import time
from threading import Thread

c1 = Client("Jim")
c2 = Client("Tim")
def update_messages():
	msgs=[]
	run = True
	while run:
		time.sleep(1)
		new_msgs = c1.get_messages()
		msgs.extend(new_msgs)
		for msg in new_msgs:
			print(msg)
			if msg=="quit":
				run = False
				break

Thread(target=update_messages).start()
time.sleep(5)
c2.send_message("hello")
time.sleep(5)
c2.send_message("whats up")
time.sleep(5)
c1.send_message("nothing much, hbu")
time.sleep(5)
c2.send_message("boring")
time.sleep(5)

c1.disconnect()
time.sleep(2)
c2.disconnect()