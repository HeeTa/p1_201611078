import math
ky=(37.575829,126.973580)
an=(37.576554,126.985164)
kw=(37.571620,126.976439)
jl=(37.570414,126.992108)
jg=(37.570164,126.983022)
locations=[ an, kw, jl, jg]
def getdistance(loc1, loc2):
    distance=math.sqrt((loc1[0]-loc2[0])**2+(loc1[1]-loc2[1])**2)
    print distance
    return distance

distance=list()

for i in locations:
    print "location is{0}".format(i)
    x=getdistance(ky,i)
    distance.append(x)

getdistance(locations[1],locations[2])
print "min distance is{0}".format(min(distance))