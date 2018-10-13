def letter2number(gradeLetter):
    gradeLetter = gradeLetter.upper()
    grades = {"A+":4.3, "A":4.0, "A-":3.7, 
              "B+":3.3, "B":3.0, "B-":2.7, 
              "C+":2.3, "C":2.0, "C-":1.7, 
              "D+":1.3, "D":1.0, "D-":0.7, 
              "F+":0.3, "F":0.0}

    return grades[gradeLetter]

agencies = {"CCC":"Civilian Conservation Corps", 
            "FCC":"Federal Communications Commission", 
            "FDIC":"Federal Deposit Insurance Corporation", 
            "SSB":"Social Security Board", 
            "WPA":"Works Progress Administration"}
#TODO add "SEC":"Securities and Exchange Commission"
#     set SSB value to "Social Security Administration"
#     remove CCC and WPA

def reverse(phonebook):
    outputDict = {}

    for i in range(len(phonebook)):
        outputDict.update({list(reversed(list(phonebook.keys())))[i]:list(reversed(list(phonebook.values())))[i]})
    
    return outputDict

def different(table):
    amtList = []

    for i in range(len(table)):
        for o in range(len(table[i])):
            if not(table[i][o] in amtList):
                amtList.append(table[i][o])

    return len(amtList)

def index(file, wordList):
    wordDict = {}
    linesList = []

    for i in range(len(wordList)):
        wordDict.update({wordList[i]:[]})
    
    reader = open(file, 'r')
    linesList = reader.readlines()
    reader.close()

    for i in range(len(linesList)):
        linesList[i] = linesList[i].lower()
        for word in wordList:
            word = word.lower()
            if (word in linesList[i]):
                wordDict[word].append(i + 1)
    
    for word in wordList:
        print(word + " " + str(wordDict[word]))
