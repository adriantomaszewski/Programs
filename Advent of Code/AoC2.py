def main():
    f = open("/Users/adrian/Documents/Programs/Advent of Code/input2.txt", "r")
    linelist = f.readlines()
    count = 0
    for line in linelist:
        ID = int(getID(line))
        if findOverCountBlue(line)==True:
            count+=0
        elif findOverCountGreen(line) == True:
            count+=0
        elif findOverCountRed(line) == True:
            count+=0
        else:
            count+=ID
    print(count)

def findOverCountBlue(line):
    blueexistcheck=1
    try:
        line.index("blue")
    except:
        blueexistcheck=0
        return False
    while blueexistcheck==1:
        blueindex=line.index("blue")
        bluevalue = int(line[blueindex-3: blueindex-1].strip())
        if bluevalue>14:
            return True
        elif bluevalue<=14:
            line=line.replace("blue", "", 1)
            if findOverCountBlue(line) == True:
                return True
            else:
                return False

def findOverCountGreen(line):
    greenexistcheck=1
    try:
        line.index("green")
    except:
        greenexistcheck=0
        return False
    while greenexistcheck==1:
        greenindex=line.index("green")
        greenvalue = int(line[greenindex-3: greenindex-1].strip())
        if greenvalue>13:
            return True
        elif greenvalue<=13:
            line=line.replace("green", "", 1)
            if findOverCountGreen(line) == True:
                return True
            else:
                return False

def findOverCountRed(line):
    redexistcheck=1
    try:
        line.index("red")
    except:
        redexistcheck=0
        return False
    while redexistcheck==1:
        redindex=line.index("red")
        redvalue = int(line[redindex-3: redindex-1].strip())
        if redvalue>12:
            return True
        elif redvalue<=12:
            line=line.replace("red", "", 1)
            if findOverCountRed(line) == True:
                return True
            else:
                return False
      
def getID(line):
    colonlocation = line.index(":")
    return line[5:colonlocation]

if __name__=="__main__":
    main()
