scoreData=[["English",100,"Math",200],["English",200,"Math",200],
           ["English",100,"Math",300]]
englishSum=0
mathSum=0
for i in scoreData:
    englishSum=i[1]+englishSum
    mathSum=i[3]+mathSum
engAver=englishSum/len(scoreData)
mathAver=mathSum/len(scoreData)
print engAver, mathAver