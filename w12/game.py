import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
geo=open("geo.txt",'r')
dist=100
for line in geo:
	if line.count('name')>0:
		fname=line[5:]
	elif line.count('go')>0:
		t1.fd(dist)
	elif line.count('right')>0:
		t1.right(int(line[6:]))
	elif line.count('left')>0:
		t1.left(int(line[5:]))
	elif line.count('loc')>0:
		loc=line[4:]
		countdown=0
		for word in loc.split():
			if countdown%2==0:
					x=int(word)
					countdown=countdown+1
			else:
					y=int(word)
					t1.goto(x,y)
					countdown=countdown+1
geo.close()
raw_input()