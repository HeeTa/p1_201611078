alldata=[['division','very satisfaction','satisfaction','normal','dissatisfaction','very dissatisfaction'],
['contents',13.1,37.1,39.6,8.7,1.5],
['method',10.6,34.6,39.5,13.4,1.9],
['relation of friends',27.1,40.0,28.5,2.9,1.5],
['relation of teacher',16.1,37.8,38.4,6.8,0.8],
['facilities',11.4,29.8,39.0,14.8,4.9],
['environment',12.2,26.5,42.0,14.9,4.4],
['major',13.5,29.7,43.4,11.1,2.4],
['school life',13.7,37.6,43.4,4.1,1.2]]
data=alldata[1:]
satisum=0
dissatisum=0
for i in data:
	satisum=satisum+i[1]+i[2]
print "average of satisfaction is "+str(satisum/(len(data)*2))
for i in data:
	dissatisum=dissatisum+i[4]+i[5]
print "average of satisfaction is "+str(dissatisum/(len(data)*2))

