def triangle(n):
    for i in range(n):
        for o in range(i+1):
            print(o, end=" ")
        print()
    pass

def mult(list0, list1):
    outputList = []
    for i in range(len(list0)):
        for o in range(len(list1)):
            outputList.append(list0[i] * list1[o])
    return outputList

def sum(table):
    outputInt = 0
    for i in range(len(table)):
        for o in range(len(table[i])):
            outputInt = outputInt + table[i][o]
    return outputInt

def sumRow(table, rowNum):
    outputInt = 0
    for i in range(len(table[rowNum])):
        outputInt = outputInt + table[rowNum][i]
    return outputInt

def sumColumn(table, columnNum):
    outputInt = 0
    for i in range(len(table)):
        outputInt = outputInt + table[i][columnNum]
    return outputInt

def doubles(numberList):
    newList = []
    for x in range(1, len(numberList)):
        if (numberList[x] == (numberList[x - 1] * 2)):
            newList.append(numberList[x])
    return newList
