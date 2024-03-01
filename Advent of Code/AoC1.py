def main():
    f = open("/Users/adrian/Documents/Programs/Advent of Code/input1.txt", "r")
    linelist = f.readlines()
    totalcount = 0
    for linestring in linelist:
        numbersinlinelist = isolateNumbersFromLineString(linestring)
        calibrationnumber = getCalibrationValuesFromNumbers(numbersinlinelist)
        totalcount+=calibrationnumber
    print(totalcount)

def isolateNumbersFromLineString(inputstring):
    numbersinlinelist = list()
    for character in inputstring:
        if character.isnumeric()==True:
            numbersinlinelist.append(int(character))
    return numbersinlinelist

def getCalibrationValuesFromNumbers(numbersinlinelist):
    if len(numbersinlinelist)>0:
        return numbersinlinelist[0]*10+numbersinlinelist[len(numbersinlinelist)-1]

if __name__=="__main__":
    main()
