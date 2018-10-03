def doubleList(listOfNumbers):
    for i in range(len(listOfNumbers)):
        listOfNumbers[i] *= 2
    pass


def acronym(stringOfWords):
    splitString = stringOfWords.split()
    outputString = ""
    for i in range(len(splitString)):
        outputString += splitString[i][0:-(len(splitString[i]) - 1)]
    outputString = outputString.upper()
    return outputString
    pass


def multiples(listOfInts, n):
    myListOfInts = listOfInts
    for i in range(len(myListOfInts)):
        myListOfInts[i] *= n
    return myListOfInts
    pass


def formatNames(inputFile, outputFile):
    formattedNames = []
    
    inputReader = open(inputFile)
    unformattedNames = inputReader.readlines()
    inputReader.close()
    
    outputWriter = open(outputFile, "a")
    outputWriter.truncate(0)
    for i in range(len(unformattedNames)):
        splitName = unformattedNames[i].split()
        if (len(splitName) > 2):
            outputWriter.write(splitName[2] + ", " + splitName[0] + " " + splitName[1][0:-(len(splitName[1]) - 1)] + ".\n")
        else:
            outputWriter.write(splitName[1] + ", " + splitName[0] + "\n")
    outputWriter.close()
    pass

from string import ascii_lowercase
def partition(listOfStrings, letter):
    lowerList = []
    lowerLetter = letter.lower()
    letterIndex = int
    outputList = []

    for i in range(len(ascii_lowercase)):
        if (lowerLetter == ascii_lowercase[i]):
            letterIndex = i
    
    for i in range(len(listOfStrings)):
        lowerList.append(listOfStrings[i].lower())
        lowerInitial = lowerList[i][0:-(len(lowerList[i]) - 1)]
        lowerIndex = int
        for o in range(len(ascii_lowercase)):
            if (lowerInitial == ascii_lowercase[o]):
                lowerIndex = o
        if (lowerIndex <= letterIndex):
            outputList.append(listOfStrings[i])
    return outputList;
    pass

def isSorted(numList):
    if (numList == sorted(numList)):
        return True
    return False

def addLineNumbers(inputFile, outputFile):
    '''Adds line numbers to every line in a new file'''
    reader = open(inputFile)
    print(type(reader))
    defaultLinesList = reader.readLines()
    reader.close()
    writer = open(outputFile, "w+")
    for i in range(len(defaultLinesList)):
        writer.write(str(i + 1) + " " + defaultLinesList[i])
    writer.close()
    pass













