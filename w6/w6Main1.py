print "Draw Triangle With Stars"
num=raw_input("input tryangle size :")
num=int(num)
for i in range (num):
	print " "*(num-i)+"*"*(i*2-1)
raw_input()