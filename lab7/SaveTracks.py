import turtle
def saveTracks():
	global tracks
	tracks.append(t1.pos())
	return tracks
def up():
	t1.fd(100)
	saveTracks()
def right():
	t1.right(90)
	saveTracks()
def left():
	t1.left(90)
	saveTracks()
def down():
	t1.back(100)
	saveTracks()
def replayTracks(tracks):
	if len(tracks)==0:
		t1.write("No Saved Track!")
		return
	t1.penup()
	t1.goto(tracks[0])
	t1.pendown()
	for i in range (len(tracks)):
		t1.goto(tracks[i])
	return
def resetTracks():
	global tracks
	tracks=[]
	t1.write("Delete Tracks!")
def usetrutle():
	global tracks
	tracks=[]
	wn=turtle.Screen()
	global t1
	t1=turtle.Turtle()
	saveTracks()
def main():
	usetrutle()
	up()
	right()
	up()
	right()
	up()
	up()
	right()
	up()
	up()
	up()
	up()
	replayTracks(tracks)
	raw_input()
if __name__ == '__main__':
	main()