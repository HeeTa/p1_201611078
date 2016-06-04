import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
point1=(100,100)
radius=50
center=(point1[0],point1[0]+radius)
t2.penup()
t2.goto((point1[0],point1[1]))
t2.pendown()
t2.circle(radius)
def getbigger(one,two):
	if one>two:
		return one
	else:
		return two
def getlower(one,two):
	if one<=two:
		return one
	else:
		return two
def isInCircle(turtlelocation,center,radius):
	x=turtlelocation[0]
	y=turtlelocation[1]
	if t1.distance(center)<=radius:
		return True
	else:
		return False
def check():
	x=t1.pos()[0]
	y=t1.pos()[1]
	if isInCircle((x,y),center,radius):	
		print "Inside"
		t1.color("Red")
	else:
		t1.color("Black")
def mousegoto(x,y):
	t1.setpos(x,y)
	check()
def up():
	t1.fd(100)
	check()
def right():
	t1.right(90)
def left():
	t1.left(90)
def down():
	t1.back(100)
	check()
wn.onkey(up,"Up")
wn.onkey(right,"Right")
wn.onkey(left,"Left")
wn.onkey(down,"Down")
wn.onclick(mousegoto)
wn.listen()
turtle.mainloop()