def indexes(myString, myChar):
    indices = []
    for i in range(len(myString)):
        if myString[i] == myChar:
            indices.append(i)
    return indices
    pass

def doubles(numberList):
    outputList = []
    for i in range(1, len(numberList)):
        if (numberList[i] == (numberList[i-1] * 2)):
            outputList.append(numberList[i])
    return outputList
    pass


def rps(play1, play2):
    play1 = play1.upper()
    play2 = play2.upper()

    if ((play1 == 'R' and play2 == "S") or (play1 == 'P' and play2 == 'R') or (play1 == 'S' and play2 == 'P')):
        return -1
    if ((play1 == 'R' and play2 == "R") or (play1 == 'P' and play2 == 'P') or (play1 == 'S' and play2 == 'S')):
        return 0
    if ((play1 == 'R' and play2 == "P") or (play1 == 'P' and play2 == 'S') or (play1 == 'S' and play2 == 'R')):
        return 1
    pass

def tableMax(table):
    mx = None
    if (len(table[0]) > 0):
        mx = table[0][0]
    else:
        return mx
    for i in range(len(table)):
        for o in range(len(table[i])):
            if (table[i][o] > mx):
                mx = table[i][o]
    return mx
    pass

def columnMins(table):
    mins = []
    for i in range(len(table[0])):
        tmpMin = None
        for o in range(len(table)):
            if ((o == 0) or (table[o][i] < tmpMin)):
                tmpMin = table[o][i]
        mins.append(tmpMin)
    return mins
    pass
