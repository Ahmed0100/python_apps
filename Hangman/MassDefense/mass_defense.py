import turtle
import random
import math
import time

wn = turtle.Screen()
wn.setup(1200,800)
wn.bgcolor("black")
wn.title("Mass Defense Game by Ahmed Mustafa")
wn.tracer(0)

number_of_defenders = 10
number_of_attackers = 50
number_of_weapon = 10
class Sprite():
	pen = turtle.Turtle()
	pen.hideturtle()
	pen.speed(0)
	pen.penup()
	def __init__(self,x,y,shape,color):
		self.x=x
		self.y=y
		self.shape=shape
		self.color=color
		self.dx = 0
		self.dy= 0
		self.speed = 0
		self.active = False
		self.heading = 0
		self.health = 10
	def render(self):
		pass
	def move(self):
		pass

	def distance(self,other):
		d = ((self.x- other.x)**2 + (self.y- other.y)**2)**0.5
		if d<11:
			return True
		else:
			return False

class Defender(Sprite):
	def __init__(self,x,y,shape,color):
		Sprite.__init__(self,x,y,shape,color)
		self.health=50

	def render(self):
		Sprite.pen.shapesize(1,1,0)
		Sprite.pen.goto(self.x,self.y)
		Sprite.pen.shape(self.shape)
		Sprite.pen.color(self.color)
		Sprite.pen.stamp()
		color = "green"

		if self.health >= 50:
			color= "green"
		elif self.health > 15:
			color = "yellow"
		else:
			color= "red"

		Sprite.pen.goto(self.x + 20 , self.y)
		Sprite.pen.pendown()
		Sprite.pen.setheading(90)
		Sprite.pen.width(3)
		Sprite.pen.color(color)
		Sprite.pen.circle(20)
		Sprite.pen.penup()
class Attacker(Sprite):
	def __init__(self,x,y,shape,color):
		Sprite.__init__(self,x,y,shape,color)

	def render(self):
		Sprite.pen.shapesize(2,2,0)
		Sprite.pen .goto(self.x,self.y)
		Sprite.pen.shape(self.shape)
		Sprite.pen.color(self.color)
		Sprite.pen.stamp()
	def move(self):
		self.dx = math.cos(self.heading * 3.14 / 180) * self.speed
		self.dy = math.sin(self.heading * 3.14 / 180) * self.speed
		self.x += self.dx
		self.y += self.dy

		if self.y > 390:
			self.heading  = random.randint(190,210)
		elif self.y < -390:
			self.heading = random.randint(140,170)

		if self.x < -600:
			self.x = random.randint(1200,1500)


class DefenderWeapon(Sprite):
	def __init__(self,x,y,shape,color):
		Sprite.__init__(self,x,y,shape,color)
		self.speed = 10
	def render(self):
		Sprite.pen.shapesize(0.2,0.2,0)

		Sprite.pen.goto(self.x,self.y)
		Sprite.pen.shape(self.shape)
		Sprite.pen.color(self.color)
		Sprite.pen.stamp()
	def move(self):
		self.dx = math.cos(self.heading * 3.14 / 180) * self.speed
		self.dy = math.sin(self.heading * 3.14 / 180) * self.speed
		self.x += self.dx
		self.y += self.dy
		if self.x > 600 or self.x <-600 or self.y > 400 or self.y<-400:
			self.x = -1000
			self.active=False
class Particle(object):
	"""docstring for Particle"""
	def __init__(self,x,y,shape,color):
		Sprite.__init__(self,x,y,shape,color)
		self.active =False
		self.speed = 20
	def render(self):
		Sprite.pen.shapesize(0.1,0.1,0)
		Sprite.pen.goto(self.x,self.y)
		Sprite.pen.shape(self.shape)
		Sprite.pen.color(self.color)
		Sprite.pen.stamp()

	def move(self):
		self.dx = math.cos(self.heading * 3.14 / 180) * self.speed
		self.dy = math.sin(self.heading * 3.14 / 180) * self.speed
		self.x += self.dx
		self.y += self.dy

		if self.x < -600 or self.x > 600 or self.y > 400 and self.y < -400:
			self.x = -1000
			self.y = 0
			self.active= False

defenders = []
defender_weapons = []
attackers= []
attacker_weapons = []
particles = []

colors = ["red","white","orange", "yellow"]

for _ in range(50):
	color = random.choice(colors)
	particles.append(Particle(-1000,0,"circle",color))
#defenders
for _ in range(number_of_defenders):
	x=random.randint(-500,-300)
	y=random.randint(-300,300)
	defenders.append(Defender(x,y,"circle", "blue"))
#attackers
for _ in range(number_of_attackers):
	x=random.randint(300,500)
	y=random.randint(-300,300)
	attackers.append(Attacker(x,y,"circle", "red"))
	attackers[-1].speed = random.randint(2,5)
	attackers[-1].heading = random.randint(160,200)

#defender_weapons
for _ in range(number_of_weapon):
	x = -1000
	y = -1000
	defender_weapons.append(DefenderWeapon(-1000,-1000,"circle", "lightblue"))
	defender_weapons[-1].active= False

def add_defenders(x, y):
	defenders.append(Defender(x,y,"circle", "blue"))
	defender_weapons.append(DefenderWeapon(x,y,"circle", "lightblue"))
	defender_weapons[-1].active= False

wn.onclick(add_defenders)

#main loop
while True:
	for defender_weapon in defender_weapons:
		if defender_weapon.active == False and len(attackers)> 0:
			defender = random.choice(defenders)
			defender_weapon.x = defender.x
			defender_weapon.y= defender.y
			defender_weapon.active= True

			#find enmey to aim at
			attacker = random.choice(attackers)
			defender_weapon.heading = math.atan2(attacker.y-defender.y,attacker.x- defender.x) * 57.298
			break
	#check for collisions
	for defender_weapon in defender_weapons:
		if defender_weapon.active == True:
			for attacker in attackers:
				if defender_weapon.distance(attacker):
					count = 0;
					for particle in particles:
						if particle.active == False:
							particle.active= True
							particle.health = random.randint(0,360)
							particle.x = defender_weapon.x
							particle.y = defender_weapon.y
							count += 1
							if count > 5:
								break
					attacker.health -= random.randint(3,7)
					if(attacker.health <= 0):
						attackers.remove(attacker)
					else:
						attacker.x += 25
					defender_weapon.x = -1000
					break

	#check for defender/attacker collision
	for defender in defenders:
			for attacker in attackers:
				if defender.distance(attacker):
					attacker.health -= random.randint(3,7)
					if(attacker.health <= 0):
						attackers.remove(attacker)
					else:
						attacker.x += 25

					defender.health -= random.randint(3,7)
					if(defender.health <= 0):
						defenders.remove(defender)
					break
	for defender_weapon in defender_weapons:
		defender_weapon.render()
		defender_weapon.move()

	for defender in defenders:
		defender.render()
		defender.move()

	for attacker in attackers:
		attacker.render()
		attacker.move()

	for particle in particles:
		particle.render()
		particle.move()
	#update 
	wn.update()
	if (len(attackers) == 0):
		print("The defenders won")
		time.sleep(3)
		exit()
	Sprite.pen.clear()
wn.mainloop()
