import turtle

win = turtle.Screen()
win.title("PingPong Game By AMUSTAFA")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)

#paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)

#paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.shape("square")
paddle2.color("red")
paddle2.penup()
paddle2.goto(350,0)
#paddle 2
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

#functions
def	paddleUp1():
	y=paddle1.ycor()
	y+=20
	paddle1.sety(y)

def paddleDown1():
	y=paddle1.ycor()
	y-=20
	paddle1.sety(y)

def	paddleUp2():
	y=paddle2.ycor()
	y+=20
	paddle2.sety(y)

def paddleDown2():
	y=paddle2.ycor()
	y-=20
	paddle2.sety(y)

#bindings
win.listen()
win.onkeypress(paddleUp1,"w")
win.onkeypress(paddleDown1,"s")
win.onkeypress(paddleUp2,"Up")
win.onkeypress(paddleDown2,"Down")
#game loop
while True:
	win.update()
