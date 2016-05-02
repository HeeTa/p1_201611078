myroom=set(['Tv','phone','camera','fridger','mixer','audio','cd player','light','computer','notebook','recoder'])
frroom=set(['coffee machine','radio','camera','running machine','ramp','computer','notebook','recoder'])
allhave= myroom&frroom
every= myroom.union(frroom)
print "only me have:"
print myroom-allhave
print "only friend have"
print frroom-allhave
print "allhave"
print allhave
print "allmachine"
print every