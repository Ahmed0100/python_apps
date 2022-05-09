from round import Round
class Chat():
	def __init__(self,r):
		self.content = []
		self.round = r

	def update(self,msg):
		self.content.append(msg)

	def get_chat(self):
		return self.content

	def __len__(self):
		return len(self.content)

	def __str__(self):
		return "".join(self.content)

	def __rebr__(self):
		return str(self)