#DOESNT WORK FUNDAMENTALLY ADDS DIGITS IN ORDER NOT THE PAIRS


import copy

def main():
    global numbers
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    f = open("/Users/adrian/Documents/Advent of Code/input3.txt", "r")
    linelist = f.readlines()
    array = list()
    totalcount = 0
    for line in linelist:
        line.rstrip()
        listofcharsinline = list()
        for char in line:
            listofcharsinline.append(char)
        array.append(listofcharsinline)
    checkarray = copy.deepcopy(array)
    adjacentarray= copy.deepcopy(array)
    isValidStarCheck(array, checkarray, adjacentarray)
    for count, number in enumerate(numberCombineIfGood(array, checkarray, adjacentarray)):
        if count%2==0:
            number1=number
        if count%2==1:
            number2=number
        if count%2==1:
            totalcount+=int(number1)*int(number2)
    print(totalcount)

def isValidStarCheck(array, checkarray, adjacentarray):
    for row,rowlist in enumerate(array):
        for column, columnvalue in enumerate(rowlist):
            if columnvalue == "*":
                adjacentcount = 0
                try:
                    if array[row-1][column-1] in numbers:
                        adjacentcount+=1
                        adjacentarray[row-1][column-1]=True
                except:
                    pass
                try:
                    if array[row][column-1] in numbers:
                        adjacentcount+=1
                        adjacentarray[row][column-1]=True
                except:
                    pass
                try:
                    if array[row+1][column-1] in numbers:
                        adjacentcount+=1
                        adjacentarray[row+1][column-1]=True
                except:
                    pass
                try:
                    if array[row-1][column] in numbers:
                        adjacentcount+=1
                        adjacentarray[row-1][column]=True
                except:
                    pass
                try:
                    if array[row+1][column] in numbers:
                        adjacentcount+=1
                        adjacentarray[row+1][column]=True
                except:
                    pass
                try:
                    if array[row-1][column+1] in numbers:
                        adjacentcount+=1
                        adjacentarray[row-1][column+1]=True
                except:
                    pass
                try:
                    if array[row][column+1] in numbers:
                        adjacentcount+=1
                        adjacentarray[row][column+1]=True
                except:
                    pass
                try:
                    if array[row+1][column+1] in numbers:
                        adjacentcount+=1
                        adjacentarray[row+1][column+1]=True
                except:
                    pass
                if adjacentcount>=2:
                    checkarray[row][column]=True
                else:
                    checkarray[row][column]=False

def numberCombineIfGood(array, checkarray, adjacentarray):
    goodnumberlist=list()
    currentnumber=""
    goodnumber=0
    for row,rowlist in enumerate(array):
        for column, columnvalue in enumerate(rowlist):
            stillnumber=columnvalue.isnumeric()
            while stillnumber==True:
                currentnumber+=columnvalue
                if adjacentarray[row][column]==True and checkIfAdjacentStarIsGood(checkarray, row, column)==True:
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

def checkIfAdjacentStarIsGood(checkarray, row, column):
    try:
        if checkarray[row-1][column-1]==True:
            return True
    except:
        pass
    try:
        if checkarray[row][column-1]==True:
            return True
    except:
        pass
    try:
        if checkarray[row+1][column-1]==True:
            return True
    except:
        pass
    try:
        if checkarray[row-1][column]==True:
            return True
    except:
        pass
    try:
        if checkarray[row+1][column]==True:
            return True
    except:
        pass
    try:
        if checkarray[row-1][column+1]==True:
            return True
    except:
        pass
    try:
        if checkarray[row+1][column]==True:
            return True
    except:
        pass
    try:
        if checkarray[row+1][column+1]==True:
            return True
    except:
        pass
    return False

if __name__=="__main__":
    main()
