def main():
    f = open("/Users/adrian/Documents/Programs/Advent of Code/input4.txt", "r")
    linelist = f.readlines()
    winnumberarray = list()
    yournumberarray = list()
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
    print(checkForRepeatsInArrays(yournumberarray, winnumberarray))

def checkForRepeatsInArrays(yournumberarray, winnumberarray):
    totalcount = 0
    for row, line in enumerate(yournumberarray):
        count=0
        for column, item in enumerate(line):
            if item in winnumberarray[row]:
                count+=1
        if count==0:
            totalcount+=0
        else:
            totalcount+=2**(count-1)
    return totalcount

if __name__=="__main__":
    main()
