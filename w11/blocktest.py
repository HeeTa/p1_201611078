import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
point1=(100,100)
point2=(200,200)
t2.penup()
t2.goto(point1)
t2.pendown()
t2.goto(point2)
def mousegoto(x,y):
	if x>point1[0] and x<point2[0] and y>point1[1] and y<point2[1]:
		print "Blocked!"

	else:
		t1.setpos(x,y)
def check(x,y):
	print "hello"
def debug():
	print "hello!"
wn.onclick(mousegoto)
wn.listen(debug)
turtle.mainloop()