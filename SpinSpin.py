


print "Spin and Bigger"
geo=raw_input("Input line number of figur that you want to draw: ")
def check(val):
	try:
		int(val)
		return 1
	except ValueError:
		print "wrong format! Plese Input Int number!"
		return 0
		raw_input("input any key to exit")
		exit()
check(geo)
size=raw_input("Input Size number of figur that you want to draw: ")
check(size)
spin=raw_input("Input Spin number of figur that you want to draw: ")
check(spin)
bigger=raw_input("Input number that size number of getting bigger: ")
check(bigger)
angle=360/int(geo)
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
for i in range(int(spin)):
	if(i%2):
		size=int(size)+int(bigger)
		print size
		t1.right(angle)
		t1.fd(int(size))
	else:
		t1.fd(int(size))
raw_input()