import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def quit():
	wn.bye()
def up():
	t1.fd(50)
def right():
	t1.right(90)
def left():
	t1.left(90)
def down():
	t1.backward(50)
def mousegoto(x,y):
	t1.setpos(x,y)
def draggoto(x,y):
	t1.setpos(x,y)
wn.onclick(mousegoto)
def addKeys():
	wn.onkey(up,"Up")
	wn.onkey(right,"Right")
	wn.onkey(left,"Left")
	wn.onkey(down,"Down")
	wn.onkey(quit,"q")
	wn.onkey(quit,"Q")
addKeys()
wn.listen()
turtle.mainloop()