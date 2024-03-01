import copy

def main():
    global symbols
    symbols = ["*","#","+","$","@","=","-","/","?", "%", "^", "&"]
    f = open("/Users/adrian/Documents/Advent of Code/input3.txt", "r")
    linelist = f.readlines()
    array = list()
    totalcount = 0
    for line in linelist:
        line.strip()
        listofcharsinline = list()
        for char in line:
            listofcharsinline.append(char)
        array.append(listofcharsinline)
    checkarray = copy.deepcopy(array)
    isValidCheck(array, checkarray)
    for number in numberCombineIfGood(array, checkarray):
        totalcount+=int(number)
    print(totalcount)

def isValidCheck(array, checkarray):
    for row,rowlist in enumerate(array):
        for column, columnvalue in enumerate(rowlist):
            valid=0
            try:
                if array[row-1][column-1] in symbols:
                    valid=1
            except:
                pass
            try:
                if array[row][column-1] in symbols:
                    valid=1
            except:
                pass
            try:
                if array[row+1][column-1] in symbols:
                    valid=1
            except:
                pass
            try:
                if array[row-1][column] in symbols:
                    valid=1
            except:
                pass
            try:
                if array[row+1][column] in symbols:
                    valid=1
            except:
                pass
            try:
                if array[row-1][column+1] in symbols:
                    valid=1
            except:
                pass
            try:
                if array[row][column+1] in symbols:
                    valid=1
            except:
                pass
            try:
                if array[row+1][column+1] in symbols:
                    valid=1
            except:
                pass
            if valid == 1:
                checkarray[row][column]=True
            else:
                checkarray[row][column]=False

def numberCombineIfGood(array, checkarray):
    goodnumberlist=list()
    currentnumber=""
    goodnumber=0
    for row,rowlist in enumerate(array):
        for column, columnvalue in enumerate(rowlist):
            stillnumber=columnvalue.isnumeric()
            while stillnumber==True:
                currentnumber+=columnvalue
                if checkarray[row][column]==True:
                    goodnumber=1
                break
            if stillnumber==False:
                if goodnumber==1:
                    goodnumberlist.append(currentnumber)
                    goodnumber=0
                    currentnumber=""
                else:
                    goodnumber=0
                    currentnumber=""
    return goodnumberlist
    
if __name__=="__main__":
    main()
