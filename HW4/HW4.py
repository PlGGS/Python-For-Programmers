def intersect(list1, list2):
    '''returns the intersection of two lists'''
    outputList = []
    
    for itemA in list1:
        for itemB in list2:
            if (itemA == itemB):
                outputList.append(itemA)
    return outputList

def pay(hourlyWage, lastWeekHours):
    '''Returns the income made by a worker based off of their amount of hours worked in the last week'''
    if (lastWeekHours <= 40):
        income = lastWeekHours * hourlyWage
    elif (lastWeekHours > 40 and lastWeekHours <= 60):
        income = (40 * hourlyWage) + ((lastWeekHours - 40) * hourlyWage * 1.5)
    elif (lastWeekHours > 60):
        income = (40 * hourlyWage) + (20 * hourlyWage * 1.5) + ((lastWeekHours - 60) * hourlyWage * 2)
        
    return income

def lastFirst(fullNamesList):
    outputLists = [[],[]]

    for i in range(len(fullNamesList)):
        outputLists[0].append(str(fullNamesList[i]).split(", ")[0])
        outputLists[1].append(str(fullNamesList[i]).split(", ")[1])

    return outputLists

def inversions(pUpperList):
    '''Returns the number of inversions in a sequence'''
    tmpSpot = 1
    amt = 0
    upperList = list(pUpperList)
    sortedList = sorted(upperList)

    while upperList != sortedList:
        if (tmpSpot < len(upperList)):
            if (upperList[tmpSpot] < upperList[tmpSpot - 1]):
                amt += 1
                tmpVal = upperList[tmpSpot - 1]
                upperList[tmpSpot - 1] = upperList[tmpSpot]
                upperList[tmpSpot] = tmpVal    
            tmpSpot += 1
        else:
            tmpSpot = 1
    
    return amt

def subList(list1, list2):
    '''Returns true if all values of the first list are also found consequtively within the second'''
    tmpIndex = 0
    
    for i in range(len(list1)):
        if (list1[i] in list2):
            if (i != len(list1) - 1):
                tmpIndex = list(list2).index(list1[i]) + 1
                list2 = list2[tmpIndex:len(list2)]
                tmpIndex = 0
        else:
            return False

    return True
