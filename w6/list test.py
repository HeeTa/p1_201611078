y=list()
def sumList(y):
	for i in range(1,1000):
		if i%4==0 and i%5!=0:
			y.append(i)
	sum=0
	for i in range(len(y)):
		sum=sum+y[i]	
	return sum
def main():
	print sumList(y)
main()
raw_input("enter to exit")