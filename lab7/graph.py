word='sangmyung university'
mydict=dict()
for i in word:
    if i not in mydict:
        mydict[i]=1
    else:
        mydict[i]=mydict[i]+1
print mydict
import matplotlib
import matplotlib.pyplot as plt

plt.bar(range(len(mydict)), mydict.values(),align='center')
plt.xticks(range(len(mydict)),list(mydict.keys()))
plt.show()
word ='7 hongji'
print len(word)
print '1'.isdigit()
print 'a'.isdigit()
print '1'.isalpha()
print 'a'.isalpha()

def countchar(word):
    mydict=dict()
    for i in word:
        if i not in mydict:
            mydict[i]=1
        else:
            mydict[i]=mydict[i]+1
    print mydict
    return mydict
def drawgraph(word):
    mydict=dict()
    for i in word:
        if i not in mydict:
            mydict[i]=1
        else:
            mydict[i]=mydict[i]+1
    plt.bar(range(len(mydict)), mydict.values(),align='center')
    plt.xticks(range(len(mydict)),list(mydict.keys()))
    plt.show()
    print mydict
    return mydict
def drawgraphwithnum(word):
    def checkkey(word):
        if word not in mydict:
            mydict[word]=1
        else:
            mydict[word]=mydict[word]+1
    mydict=dict()
    for i in word:
        if i.isdigit():
            checkkey('digit')
        else:
            checkkey('alpha')
    plt.bar(range(len(mydict)), mydict.values(),align='center')
    plt.xticks(range(len(mydict)),list(mydict.keys()))
    plt.show()
    print mydict
    return mydict
drawgraphwithnum("123456asdfg")
