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
    inputstring=inputstring.replace("twone","21")
    inputstring=inputstring.replace("oneight","18")
    inputstring=inputstring.replace("threeight","38")
    inputstring=inputstring.replace("nineight","98")
    inputstring=inputstring.replace("sevenine","79")
    inputstring=inputstring.replace("eightwo","82")
    inputstring=inputstring.replace("one","1")
    inputstring=inputstring.replace("two","2")
    inputstring=inputstring.replace("three","3")
    inputstring=inputstring.replace("four","4")
    inputstring=inputstring.replace("five","5")
    inputstring=inputstring.replace("six","6")
    inputstring=inputstring.replace("seven","7")
    inputstring=inputstring.replace("eight","8")
    inputstring=inputstring.replace("nine","9")
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
