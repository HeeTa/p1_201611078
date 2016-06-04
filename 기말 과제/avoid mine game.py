import turtle
import time
import math
import random
def showRec():
	try:
		record=open('minegameRecord.txt','r')
	except:
		error=1
	else:
		scorelist=list()
		datalist=list()
		for line in record.readlines():
			datalist.append(line)
			x=0
			for word in line.split():
				x=x+1
				if x%4==0:
					gScore=word
					scorelist.append(gScore)
		highScore=max(scorelist)
		print "Your Highest Score is {0}".format(highScore)
		print "[     Play Date     ][bomb][Score][clear?]"
		for i in datalist:
			print i
		record.close()

def minegame():
	class player(turtle.Turtle):
		alive=True
		def setAlive(self,arg):
			self.alive=arg
		def getAlive(self):
			return self.alive
	print "Avoid Mine Game"
	print "Win The Game by Going Outside of the Screen!"
	showRec()
	print "Recommended mine number is over 50"
	global minenum
	minenum=raw_input("Input the number of mines : ")
	try:
		int(minenum)
	except ValueError as e:
		print e
		raw_input()
		exit()
	
	minenum=int(minenum)
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
	    while abs(randomx)<30 and abs(randomy)<30:
			randomx=random.randrange(-250,250)
			randomy=random.randrange(-250,250)
	    mines[i].setpos(randomx,randomy)
	player=player()
	player.color("white")
	player.pencolor("black")
	player.shape("turtle")
	global score
	score=500+(minenum*500)
	scoreT=turtle.Turtle()
	scoreT.color("red")
	scoreT.penup()
	scoreT.setpos(0,200)
	def writeRec():
		recorda=open('minegameRecord.txt','a')
		date=time.strftime('[%Y-%m-%d %H:%M:%S]')
		if player.getAlive():
			life="Clear"
		else:
			life="Fail"
		text="{0} {1} {2} {3}\n".format(date,minenum,score,life)
		recorda.write(text)
	def checkdis(player):
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
	def clear():
		if player.getAlive():
			print "CLEAR!\n Congraturation!"
		writeRec()
		player.setAlive(False)
		


	def writeShortest():
		checkdis(player)
		if getshortest()<=45 and getshortest()>35:
			player.write("Mine is near!")
			player.color("yellow")
			player.pencolor("black")
		elif getshortest() <= 35 and getshortest()>20:
			player.write("Mine is Too near! Move Away!")
			player.color("orange")
			player.pencolor("black")
		elif getshortest() <= 20:
			player.write("BOOM!!!!! Game Over!")
			player.color('red')
			player.pencolor("black")
			print "GameOver!"
			showRec()
			player.setAlive(False)
			writeRec()
			for i in range(minenum):
				mines[i].showturtle()
		else:
			player.write(getshortest())
			player.color("white")
			player.pencolor("black")
			checkPlayerLoc()
	def checkPlayerLoc():
		if abs(player.pos()[0])>=250 or abs(player.pos()[1])>=250:
			clear()
			
	def writeScore():
		global score
		score=score-50
		scoreT.clear()
		scoreT.write("Score: "+str(score))
	writeScore()
	def up():
		if player.getAlive():
			player.fd(10)
			player.clear()
			writeShortest()
			writeScore()
	def right():
		if player.getAlive():
			player.right(90)
	def left():
		if player.getAlive():
			player.left(90)
	def back():
		if player.getAlive():
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
	turtle.mainloop()
def main():
	minegame()
if __name__=="__main__":
	main()