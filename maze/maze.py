import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)

levels = [""]
levle_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX         XXXXXX",
"X  XXXXXXX  XXXXX  XXXXXX",
"X  XXXXXXX  XXXXX  XXXXXX",
"X     XXXX         XXXXXX",
"X  XX XXXX         XXXXXX",
"XXXXX XXXX         XXXXXX",
"XXXXX       XXXXX  XXXXXX",
"X  XXXXXXXXXXXXXX  XXXXXX",
"X  XXXXXXXXX       XXXXXX",
"X  XXXXXXX         XXXXXX",
"X  XXXXXXX E       XXXXXX",
"X  XXXXXXXXXXXXXX  XXXXXX",
"X  XXXXXXX  XXXXX  XXXXXX",
"X  XXXXXXX         XXXXXX",
"X  XXXXX           XXXXXX",
"X  XXXXX E         XXXXXX",
"X  XXXXX XXXXXXXXXXXXXXXX",
"X  XXXXX XXXXXXXXXXXXXXXX",
"X  XXXXX       E  XXXXXXX",
"X  XXXXXX         XXXXXXX",
"X  XXXXXXX         XXXXXX",
"X  XXXXXXX  XXXXXT XXXXXX",
"X  XXXXXXX  XXXXX  XXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

levels.append(levle_1)

shapes = ["player.gif", "wall.gif","treasure.gif","invader.gif"]
for shape in shapes:
	turtle.register_shape(shape)

class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("white")
		self.penup()
		self.speed(0)

class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("player.gif")
		self.color("blue")
		self.penup()
		self.speed(0)
		self.gold =0

	def go_up(self):
		new_x = self.xcor()
		new_y = self.ycor() + 24
		if(new_x,new_y) not in walls:
			self.goto(new_x,new_y)

	def go_down(self):
		new_x = self.xcor()
		new_y = self.ycor() - 24
		if(new_x,new_y) not in walls:
			self.goto(new_x,new_y)

	def go_left(self):
		new_x = self.xcor()-24
		new_y = self.ycor()
		if(new_x,new_y) not in walls:
			self.goto(new_x,new_y)
			self.shape("player.gif")

	def go_right(self):
		new_x = self.xcor() + 24
		new_y = self.ycor()
		if(new_x,new_y) not in walls:
			self.goto(new_x,new_y)
			self.shape("player.gif")

	def is_collision(self,other):
		a = self.xcor() - other.xcor()
		b = self.ycor() - other.ycor()
		dist = math.sqrt((a**2) + (b**2))
		if dist < 5:
			return True
		else:
			return False

class Enemy(turtle.Turtle):
	def __init__(self,x,y):
		turtle.Turtle.__init__(self)
		self.shape("invader.gif")
		self.color("red")
		self.penup()
		self.speed(0)
		self.gold = 25
		self.goto(x,y)
		self.direction = random.choice(["up", "down", "left", "right"])
	def move(self):
		if self.direction == "up":
			dx = 0
			dy = 24
		elif self.direction == "down":
			dx = 0
			dy = -24
		elif self.direction == "left":
			dx = -24
			dy = 0
		elif self.direction == "right":
			dx = 24
			dy = 0
		else:
			dx = 0
			dy = 0
		if(self.is_close(player)):
			if(player.xcor() < self.xcor()):
				self.direction = "left"
			elif player.xcor() > self.xcor():
				self.direction = "right"
			elif player.ycor() > self.ycor():
				self.direction = "up"
			elif player.ycor() < self.ycor():
				self.direction = "down"

		new_x = self.xcor() + dx
		new_y = self.ycor() + dy

		if((new_x,new_y) not in walls):
			self.goto(new_x,new_y)
		else:
			self.direction = random.choice(["up","down","left","right"])

		turtle.ontimer(self.move,t=random.randint(100,300))

	def is_close(self,other):
		a = self.xcor() - other.xcor()
		b = self.ycor() - other.ycor()
		dist = math.sqrt((a**2) + (b**2))
		if dist < 75:
			return True
		else:
			return False

	def destroy(self):
		self.goto(2000,2000)
		self.hideturtle()

class Treasure(turtle.Turtle):
	def __init__(self,x,y):
		turtle.Turtle.__init__(self)
		self.shape("treasure.gif")
		self.color("gold")
		self.penup()
		self.speed(0)
		self.gold = 100
		self.goto(x,y)
	def destroy(self):
		self.goto(2000,2000)
		self.hideturtle()


def setup_maze(levels):
	for y in range(len(levels)):
		for x in range(len(levels[y])):
			char = levels[y][x]
			screen_x=-288 + x*24
			screen_y = 288 - y*24
			if char == 'X':
				pen.goto(screen_x,screen_y)
				pen.shape("wall.gif")
				pen.stamp()
				walls.append((screen_x,screen_y))
			if char == 'P':
				player.goto(screen_x,screen_y)
			if char =='T':
				treasures.append(Treasure(screen_x,screen_y))
			if char =='E':
				enemies.append(Enemy(screen_x,screen_y))
#create walls
walls = []

treasures = []
enemies = []
#create objects
pen = Pen()
player = Player()
setup_maze(levels[1])

turtle.listen()
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")

wn.tracer(0)

for enemy in enemies:
	turtle.ontimer(enemy.move, t=250)

while True:
	for treasure in treasures:
		if player.is_collision(treasure):
			player.gold += treasure.gold
			print("Player Gold {}".format(player.gold))
			treasure.destroy()
			treasures.remove(treasure)

	for enemy in enemies:
		if player.is_collision(enemy):
			print("Player dies")

	wn.update()
