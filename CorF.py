print "Temperature changing program"
print "input C or F to Choose"
sel=raw_input("input :")
if(sel=='C'):
	print "you select C"
else:
	if(sel=='F'):
		print "you select F"
	else:
		print "You have input wrong text"
		raw_input("Press Enter to Exit")
		exit()

tem=raw_input("input temperature :")
if(sel=='C'):
	tem=(float(tem)*1.8)+32
	print tem
else:
	tem=(float(tem)-32)/1.8
	print tem

raw_input("Press Enter to Exit")
exit()