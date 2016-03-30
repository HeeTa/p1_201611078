score=raw_input("Input Score(0~100: ")
def check(val):
	try:
		float(val)
	except ValueError:
		print "wrong format! Plese Input Float number!"
		raw_input("input any key to exit")
		exit()

check(score)
score=float(score)
if 90<score<=100:
    grade="A"
elif 80<score<=90:
    grade="B"
elif 70<score<=80:
    grade="C"
elif 60<score<=80:
    grade="D"
else:
    grade="F"
print "Grade is %s"%grade
raw_input("input any key to exit")