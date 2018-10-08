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

def inversions(upperList):
    '''Returns the number of inversions in a sequence'''
    amt = 0
    sortedList = sorted(upperList)

    for i in range(len(upperList)):
        itemA = upperList[i]
        itemB = sortedList[i]
        if (itemA != itemB):
                amt += 1
    return int(amt/2)