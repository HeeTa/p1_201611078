import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
point1=(100,100)
point2=(200,-200)
t2.penup()
t2.goto((point1[0],point1[1]))
t2.pendown()
t2.goto((point1[0],point2[1]))
t2.goto((point2[0],point2[1]))
t2.goto((point2[0],point1[1]))
t2.goto((point1[0],point1[1]))
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
def isInRectangle(turtlelocation,boxpoints):
	x=turtlelocation[0]
	y=turtlelocation[1]
	x1=boxpoints[0][0]
	x2=boxpoints[1][0]
	y1=boxpoints[0][1]
	y2=boxpoints[1][1]
	x3=getlower(x1,x2)
	x4=getbigger(x1,x2)
	y3=getlower(y1,y2)
	y4=getbigger(y1,y2)
	if x>x3 and x<x4 and y>y3 and y<y4:
		return True
	else:
		return False
def check():
	x=t1.pos()[0]
	y=t1.pos()[1]
	if isInRectangle((x,y),(point1,point2)):	
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