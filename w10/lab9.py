%matplotlib inline
import math
import matplotlib
import matplotlib.pyplot as plt
jongro=(80531,83291)
joongo=(66755,67574)
youngsan=(121027,126882)
sudong=(151459,153606)
gwangjin=(183436,191744)
dongdemoon=(185827,187997)
joongrang=(208393,210227)
sungbook=(229183,240377)
gangbook=(164337,170089)
dobong=(173804,179437)
nowon=(281538,296683)
unpyung=(244964,257614)
sudemoon=(156130,166975)
mapho=(190957,207394)
yangchun=(242074,246936)
gangsu=(291216,304475)
gooro=(228201,226403)
youngdungpo=(210388,207423)
dongjak=(202165,210609)
gwanak=(266773,262258)
sucho=(217036,234222)
ganganam=(279209,302551)
songpa=(325950,341530)
gangdong=(230851,232470)
data={"jongro":jongro,"joongo":joongo,"youngsan":youngsan,"sucho":sucho,"sudong":sudong,"ganganam":ganganam,"gwangjin":gwangjin,"dongdemoon":dongdemoon,"joongrang":joongrang,"sungbook":sungbook,"gangbook":gangbook,"dobong":dobong,"nowon":nowon,"unpyung":unpyung,"sudemoon":sudemoon,"mapho":mapho,"yangchun":yangchun,"gangsu":gangsu,"gooro":gooro,"youngdungpo":youngdungpo,"dongjak":dongjak,"gwanak":gwanak,"songpa":songpa,"gangdong":gangdong}
data
popul=dict()
for i in data:
    popul[str(i)]=data[i][0]+data[i][1]
print popul
plt.bar(range(len(popul)), popul.values(), align='center')
plt.xticks(range(len(popul)),list(popul.keys()))
plt.show()