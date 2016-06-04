import turtle
wn=turtle.Screen()
wn.bgpic("bg.gif")
t1=turtle.Turtle()
def up():
	t1.fd(100)
def right():
	t1.right(90)
def left():
	t1.left(90)
def down():
	t1.back(100)
wn.onkey(up,"Up")
wn.onkey(right,"Right")
wn.onkey(left,"Left")
wn.onkey(down,"Down")
wn.listen()
turtle.mainloop()