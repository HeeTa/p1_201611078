print "BMI Calculator"


def check(val):
	try:
		float(val)
	except ValueError:
		print "wrong format! Plese Input Int number!"
		raw_input("input any key to exit")
		exit()

mass=raw_input("Input mass in Kg: ")
check(mass)
stature=raw_input("Input stature in M: ")
check(stature)

BMI=float(mass)/(float(stature)*float(stature))
print BMI

if BMI<=18.5:
	res="Underweight"
elif BMI>18.5 and BMI<25:
	res="Normal weight"
elif BMI>=25 and BMI<30:
	res="Over weight"
else:
	res="Obesity"
print res

raw_input()