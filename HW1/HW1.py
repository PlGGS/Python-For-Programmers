def computeTuition():
    numHours = int(input("Number of credit hours: "))
    cost = int(input("Cost per credit hour: "))
    
    return cost * numHours;
pass


def createStr(character, number):
	char = character[0];
	num = number;
	output = ""
	for i in range(0, int(num)):
	    output += char

	return output
pass

def sequences():
    for i in range(18, 52, 2):
        print(i, end=' ')
    print("\n")
    for i in range(27, 99, 9):
        print(i, end=' ')
    print("\n")
    for i in range(40, 8, -4):
        print(i, end=' ')
pass

def printAllBut(exclude):
    inputList = list(eval(input("Type a list of strings please: ")))
    outputList = []
    
    for i in range(len(list(inputList))):
        if (inputList[i].lower() != exclude.lower()):
            outputList.append(inputList[i])
            
    print(outputList)
pass


def printNth(n):
    inputList = list(eval(input("Type a list please: ")))
    try:
        print(inputList[n])
    except:
        pass
pass
