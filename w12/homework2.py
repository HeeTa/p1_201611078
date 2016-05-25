data=[1,2,3,4,5,6,7,8,9,10]
fout=open('outputNumber.txt','w')
def writeline(data):
    for i in data:
        if i%2==0:
            sym='\n'
        else:
            sym='\t'
        toPrint="{0}{1}".format(i,sym)
        fout.write(toPrint)
    fout.write('\n')
writeline(data)

fout.close()