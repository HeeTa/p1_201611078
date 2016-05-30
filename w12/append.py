try:
    pythonFile=open("python.txt",'a')
    arreyFile=open("outputNumber.txt",'r')
    for line in arreyFile:
        pythonFile.write(line)
    arreyFile.close()
    pythonFile.close()
except Exception as e:
    print e