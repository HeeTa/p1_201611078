def writeTrackTest():
	import turtle
	wn=turtle.Screen()
	t1=turtle.Turtle()
	tracks=list()
	def addtracks():
		tracks.append(t1.pos())
	def drawAt(x,y,linenum):
		lines=360/(linenum)
		doN=0
		print lines
		t1.penup()
		t1.setpos(x,y)
		t1.pendown()
		while doN<float(linenum):
			t1.left(lines)
			t1.fd(100)
			addtracks()
			doN=doN + 1
	drawAt(100,200,4)
	print tracks
	wn.exitonclick()
def main():
	writeTrackTest()
if __name__ == '__main__':
	main()