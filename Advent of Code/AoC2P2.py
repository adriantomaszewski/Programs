import sys

def main():
    f = open("/Users/adrian/Documents/Advent of Code/input2.txt", "r")
    linelist = f.readlines()
    count = 0
    for line in linelist:
            count+=findLeastBlue(line)*findLeastRed(line)*findLeastGreen(line)
    print(count)

def findLeastBlue(line):
    blueexistcheck=1
    leastbluevalue=-sys.maxsize-1
    try:
        line.index("blue")
    except:
        blueexistcheck=0
        return 0
    while blueexistcheck==1:
        for x in range(0, line.count("blue")):
            blueindex=line.index("blue")
            bluevalue = int(line[blueindex-3: blueindex-1].strip())
            if bluevalue>leastbluevalue:
                leastbluevalue=bluevalue
            line=line.replace("blue", "", 1)
        return leastbluevalue

def findLeastRed(line):
    redexistcheck=1
    leastredvalue=-sys.maxsize-1
    try:
        line.index("red")
    except:
        redexistcheck=0
        return 0
    while redexistcheck==1:
        for x in range(0, line.count("red")):
            redindex=line.index("red")
            redvalue = int(line[redindex-3: redindex-1].strip())
            if redvalue>leastredvalue:
                leastredvalue=redvalue
            line=line.replace("red", "", 1)
        return leastredvalue

def findLeastGreen(line):
    greenexistcheck=1
    leastgreenvalue=-sys.maxsize-1
    try:
        line.index("green")
    except:
        greenexistcheck=0
        return 0
    while greenexistcheck==1:
        for x in range(0, line.count("green")):
            greenindex=line.index("green")
            greenvalue = int(line[greenindex-3: greenindex-1].strip())
            if greenvalue>leastgreenvalue:
                leastgreenvalue=greenvalue
            line=line.replace("green", "", 1)
        return leastgreenvalue

if __name__=="__main__":
    main()
