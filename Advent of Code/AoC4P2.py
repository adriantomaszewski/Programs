# I give up

def main():
    global totalcount
    totalcount=0
    f = open("/Users/adrian/Documents/Advent of Code/testinput.txt", "r")
    linelist = f.readlines()
    winnumberarray = list()
    yournumberarray = list()
    repeatlines = list()
    for line in linelist:
        numbertoadd=""
        stillnumber=0
        line=line[8:len(line)]
        templist=list()
        for index, char in enumerate(line):
            if char=='|':
                breaklocation=index+8
                break
            if char.isnumeric()==True:
                stillnumber=1
                numbertoadd+=char
            else:
                stillnumber=0
            if stillnumber==0 and numbertoadd!="":
                templist.append(numbertoadd)
                numbertoadd=""
                index+=1
        yournumberarray.append(templist)
    for line in linelist:
        numbertoadd=""
        stillnumber=0
        line=line[breaklocation:len(line)]
        templist=list()
        for index, char in enumerate(line):
            if char.isnumeric()==True:
                stillnumber=1
                numbertoadd+=char
            else:
                stillnumber=0
            if stillnumber==0 and numbertoadd!="":
                templist.append(numbertoadd)
                numbertoadd=""
        winnumberarray.append(templist)
    for row, line in enumerate(yournumberarray):
        for x in range(0,checkForRepeatsInArrays(yournumberarray, winnumberarray, row, line)):
            repeatlines.append(yournumberarray[row+1+x])
            repeatlines.append(winnumberarray[row+1+x])
    while len(repeatlines>0):
        for arrayindex, array in enumerate(repeatlines):
            if arrayindex%2==0:
                count=0
                for column, item in enumerate(repeatlines[arrayindex]):
                    if item in repeatlines[arrayindex+1]:
                        count+=1
                        totalcount+=1
        for x in range(0,count):
            repeatlines.append(repeatlines[row+1+x])
            repeatlines.append(repeatlines[row+1+x])        
    print(repeatlines)

def checkForRepeatsInArrays(yournumberarray, winnumberarray, row, line):
    global totalcount
    count=0
    for column, item in enumerate(line):
        if item in winnumberarray[row]:
            count+=1
            totalcount+=1
    return count

if __name__=="__main__":
    main()
