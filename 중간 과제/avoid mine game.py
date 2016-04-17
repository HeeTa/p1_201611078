def minegame():
	print "Avoid Mine Game"
	print "Recommended mine number is over 50"
	minenum=input("Input the number of mines : ")
	import turtle
	import random
	import math
	turtle.setup(500,500)
	mines=[]
	minedis=[]
	wn=turtle.Screen()
	wn.bgpic("groundimg.gif")
	print "Creating Mines..."
	for i in range(minenum):
	    mines.append("mine"+str(i))
	    minedis.append(0)
	    mines[i]=turtle.Turtle()
	    mines[i].penup()
	    mines[i].hideturtle()
	    randomx=random.randrange(-250,250)
	    randomy=random.randrange(-250,250)
	    while abs(randomx)<30:
			randomx=random.randrange(-250,250)
	    mines[i].setpos(randomx,randomy)
	player=turtle.Turtle()
	player.color("white")
	player.pencolor("black")
	player.shape("turtle")
	global alive
	alive=True
	global score
	score=0
	scoreT=turtle.Turtle()
	scoreT.color("red")
	scoreT.penup()
	scoreT.setpos(0,200)
	def checkdis():
		for i in range(minenum):
			dis1=player.pos()-mines[i].pos()
			dis2=dis1[0]**2+dis1[1]**2
			dis2=math.sqrt(dis2)
			minedis[i]=dis2
	def getshortest():
		shortest=125000
		for i in range(minenum):
			if shortest> minedis[i]:
				shortest=minedis[i]
		return shortest
	def writeShortest():
		checkdis()
		if getshortest()<=45 and getshortest()>35:
			player.write("Mine is near!")
		elif getshortest() <= 35 and getshortest()>20:
			player.write("Mine is Too near! Move Away!")
		elif getshortest() <= 20:
			player.write("BOOM!!!!! Game Over!")
			print "GameOver!"
			global alive
			alive=False
			for i in range(minenum):
				mines[i].showturtle()
		else:
			player.write(getshortest())
	def writeScore():
		global score
		score=score+100
		scoreT.clear()
		scoreT.write("Score: "+str(score))
	writeScore()
	def up():
		if alive==True:
			player.fd(10)
			player.clear()
			writeShortest()
			writeScore()
	def right():
		if alive==True:
			player.right(90)
			writeShortest()
	def left():
		if alive==True:
			player.left(90)
			writeShortest()
	def back():
		if alive==True:
			player.back(10)
			player.clear()
			writeShortest()
			writeScore()
	print "GameStart!"
	wn.onkey(up,"Up")
	wn.onkey(right,"Right")
	wn.onkey(left,"Left")
	wn.onkey(back,"Down")
	wn.listen()
	wn.exitonclick()
def main():
	minegame()
if __name__=="__main__":
	main()