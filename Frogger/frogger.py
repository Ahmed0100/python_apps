import turtle
import math
import time
import random

wn = turtle.Screen()
wn.title("Frogger by amustafa")
wn.setup(600,800)
wn.bgcolor("green")
wn.bgpic("background.gif")
wn.tracer(0)

shapes = ["frog.gif", "car_left.gif", "car_right.gif", "log_full.gif",
 "log_half.gif", "turtle_left.gif", "turtle_right.gif",
 "turtle_right_half.gif", "turtle_left_half.gif",
  "turtle_submerged.gif", "goal.gif", "frog_home.gif"]

for shape in shapes:
	wn.register_shape(shape)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

class Sprite():
	def __init__(self, x, y, width, height, image):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.image = image
	def render(self,pen):
		pen.goto(self.x,self.y)
		pen.shape(self.image)
		pen.stamp()

	def update(self):
		pass
	def is_collision(self, other):
		# Axis Aligned Bounding Box
		x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
		y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
		return (x_collision and y_collision)

class Player(Sprite):
	def __init__(self, x, y, width, height, image,dx):
		Sprite.__init__(self,x,y,height,width,image)
		self.dx=0
		self.collision=False
		self.frog_home = 0
	def up(self):
		self.y +=  45

	def down(self):
		self.y -= 45

	def left(self):
		self.x -= 45

	def right(self):
		self.x += 45

	def player_restart(self):
		self.dx=0
		self.x=0
		self.y=-350
	def update(self):
		self.x += self.dx
		if(self.x < -400 or self.x > 400):
			self.x = 0
			self.y = -350

class Car(Sprite):
	def __init__(self, x, y, height, width, image,dx):
		Sprite.__init__(self,x,y,height,width,image)
		self.dx = dx

	def up(self):
		self.y +=  45

	def down(self):
		self.y -= 45

	def left(self):
		self.x -= 45

	def right(self):
		self.x += 45

	def update(self):
		self.x += self.dx
		if self.x < -400:
			self.x = 400
		if self.x >400:
			self.x = -400

class Log(Sprite):
	def __init__(self, x, y, height,width, image,dx):
		Sprite.__init__(self,x,y,height,width,image)
		self.dx = dx

	def update(self):
		self.x += self.dx
		if self.x < -400:
			self.x = 400
		if self.x >400:
			self.x = -400

class Turtle(Sprite):
	def __init__(self, x, y, width, height, image,dx):
		Sprite.__init__(self,x,y,height,width,image)
		self.dx = dx
		self.state = "full"
		self.full_time= random.randint(8,12)
		self.half_time = random.randint(4,6)
		self.submerged_time = random.randint(4,6)
		self.start_time = time.time()

	def update(self):
		self.x += self.dx
		if self.x < -400:
			self.x = 400
		if self.x >400:
			self.x = -400
		if self.state == "full":
			if self.dx > 0:
				self.image = "turtle_right.gif"
			else:
				self.image = "turtle_left.gif"
		elif self.state == "half_down" or self.state == "half_up":
			if self.dx > 0:
				self.image = "turtle_right_half.gif"
			else:
				self.image = "turtle_left_half.gif"
		elif self.state == "submerged":
			self.image = "turtle_submerged.gif"

		#timer stuff
		if self.state == "full" and time.time()-self.start_time > self.full_time:
			self.state="half_down"
			self.start_time = time.time()
		elif self.state == "half_down" and time.time()-self.start_time > self.half_time:
			self.state="submerged"
			self.start_time = time.time()
		elif self.state == "submerged" and time.time()-self.start_time > self.submerged_time:
			self.state="half_up"
			self.start_time = time.time()
		elif self.state == "half_up" and time.time()-self.start_time > self.submerged_time:
			self.state="full"
			self.start_time = time.time()


class Home(Sprite):
	def __init__(self, x, y, width, height, image):
		Sprite.__init__(self,x,y,height,width,image)

#create objects
player = Player(0,-350,40,40,"frog.gif",0)

level_1 = [
	Car(0,-300,121,40,"car_left.gif",-0.1),
	Car(0,-250,121,40,"car_right.gif",0.1),
	Car(221,-250,121,40,"car_right.gif",0.1),
	Car(0,-200,121,40,"car_left.gif",-0.1),
	Car(0,-150,121,40,"car_right.gif",0.1),
	Car(0,-100,121,40,"car_left.gif",-0.1),
	Log(0,0,161,40,"log_full.gif",-0.2),
	Log(0,50,161,40,"log_full.gif",0.2),
	Turtle(200,100,155,40,"turtle_left.gif", -0.15),
	Turtle(0,150,250,40,"turtle_left.gif", 0.15),
	Log(0,200,250,40,"log_full.gif",0.2)]

homes =[
	Home(200,250,50,50,"goal.gif"),
	Home(100,250,50,50,"goal.gif"),
	Home(0,250,50,50,"goal.gif"),
	Home(-100,250,50,50,"goal.gif"),
	Home(-200,250,50,50,"goal.gif")]


sprites = level_1 + homes
sprites.append(player)
#keyborard 
wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.left, "Left")
wn.onkeypress(player.right, "Right")

##################

while True:
	for sprite in sprites:
		sprite.render(pen)
		sprite.update()

	player.dx=0
	player.collision = False
	for sprite in sprites:
		if player.is_collision(sprite):
			if isinstance(sprite, Car):
				player.player_restart()
				break
			elif isinstance(sprite, Log):
				player.dx=sprite.dx
				player.collision = True
				break
			elif isinstance(sprite, Turtle) and sprite.state != "submerged":
				player.dx=sprite.dx
				player.collision = True
				break
			elif isinstance(sprite, Home):
				sprite.image= "frog_home.gif"
				player.player_restart()
				player.frog_home += 1



	if player.y > 0 and player.collision != True:
		player.player_restart()
	if player.frog_home == 5:
		player.player_restart()
		for home in homes:
			home.image="goal.gif"
	wn.update()
	pen.clear()

wn.mainloop()
