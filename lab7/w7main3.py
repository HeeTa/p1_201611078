def drawWithText():
	import turtle
	wn=turtle.Screen()
	t1=turtle.Turtle()
	shapes={'tryangle':3,'square':4,'pentagon':5,'hexagon':6}
	def drawAt(x,y,text):
		linenum=shapes[str(text)]
		lines=360/(linenum)
		doN=0
		t1.penup()
		t1.setpos(x,y)
		t1.pendown()
		while doN<float(linenum):
			t1.left(lines)
			t1.fd(100)
			doN=doN + 1
	drawAt(-200,-300,"tryangle")
	drawAt(100,200,"square")
	drawAt(-100,-200,"pentagon")
	x=[(0,0),(0,50),(50,50),(50,0),(0,0)]
	def drawpath(path):
		t1.penup()
		t1.goto(path[1])
		t1.pendown()
		for i in range(len(path)):
			t1.goto(path[i])
	drawpath(x)
	wn.exitonclick()
def main():
	drawWithText()
if __name__ == '__main__':
	main()
