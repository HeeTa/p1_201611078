allData =[["Coffee","Water","Milk","Icecream"],
["Espresso","No","No","No"],
["Long Black","Yes","No","No"],
["Flat White","No","Yes","No"],
["Cappuccino","No","Yes - Frothy","No"],
["Affogato","No","No","Yes"]]
data=allData[1:]
perc=0
for i in data:
    if i[2].count("Yes"):
        perc=perc+100/len(data)
print "Milk",perc,"%"