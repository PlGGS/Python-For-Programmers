def intersect(list1, list2):
    '''returns the intersection of two lists'''
    outputList = []
    alreadyInOutput = False
    
    for itemA in list1:
        for itemB in list2:
            if (itemA == itemB):
                for itemC in outputList:
                    if (itemA == itemC):
                        alreadyInOutput = True
                if (alreadyInOutput == False):
                    outputList.append(itemA)
                    
    return outputList

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