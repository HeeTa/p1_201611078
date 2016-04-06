"""
@author shc
@since 160406
@leap year programing
"""
def sayHello():
    print "I say hello!"

def sayHelloHelp(name):
	"""
	sayHello function with comments
	parameters
	----------
	arg1: str
		name
	Returns
	-------
	none
	Examples
	--------
	sayHelloHelp('jsl')
	"""
	print name, "say hello!"

def lab3():
	"""
	lab3 means lab for wk3
	do not add arguments for lab functions
	"""
	sayHello()
	sayHelloHelp("jsl")

def lab6_1():
	sum=0
	for i in range(1000):
		if i%3==0 or i%5==0:
			sum=sum+i
	print sum
def checkleap(year):
	if (year%4==0) and (year%100!=0 or year%400==0):
		print "It is Leap Year"
	else:
		print "It is not Leap Year"
def lab6_2():
	print "Checking Leap Year"
	year=input("input year: ")
	checkleap(year)
	return year
def upanddown():
	min=1
	max=10
	trynum=max/2
	num=input("Input Number: ")
	repeattime=0
	while num!=trynum:
		if num>trynum:
			trynum=trynum+trynum/2
		else:
			trynum=trynum-trynum/2
		repeattime=repeattime+1
	print "repeattime is "+str(repeattime)


def main():
	lab3()
	lab6_1()
	lab6_2()
	upanddown()

main()
raw_input()
if __name__=="__main__":
    main()